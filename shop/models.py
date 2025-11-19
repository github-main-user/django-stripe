from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the item")
    description = models.TextField(help_text="Description of the item")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Price of the item in US dollars"
    )

    def __str__(self) -> str:
        return f"Item: {self.name} by {self.price}$"
