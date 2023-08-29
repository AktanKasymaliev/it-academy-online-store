from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GoodsType(models.TextChoices):
    CLOTHES = "CL", "Clothes"
    ELECTRONICS = "EL", "Electronics"
    ACCESSORIES = "ACC", "Accessories"
    ESTATE = "EST", "Estate"


class ShopGoods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=32, decimal_places=4)
    image = models.ImageField(blank=True, null=True)
    from_at = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=GoodsType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goods")
