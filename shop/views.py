from decimal import Decimal

import stripe
from decouple import config
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from .models import Item

stripe.api_key = config("STRIPE_SECRET_KEY")


@require_GET
def item_page(request: HttpRequest, pk) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)
    publishable_key = config("STRIPE_PUBLISHABLE_KEY")
    return render(
        request, "shop/item.html", {"item": item, "stripe_pk": publishable_key}
    )


@require_GET
def create_checkout_session(request: HttpRequest, pk) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)

    amount = int((item.price * Decimal("100")).quantize(Decimal("1")))
    domain = request.build_absolute_uri("/")[:-1]  # scheme+host

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": item.currency,
                        "product_data": {
                            "name": item.name,
                            "description": item.description[:300],
                        },
                        "unit_amount": amount,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=domain + "/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain + f"/item/{item.pk}/?canceled=true",
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"session_id": session.id})
