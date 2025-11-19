from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ("usd", "USD"),
        ("eur", "EUR"),
        ("rub", "RUB"),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="usd")

    def __str__(self):
        return f"{self.name} — {self.price} {self.currency.upper()}"
