from django import forms

from .models import ShopGoods


class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = ShopGoods
        fields = ("title", "description", "price", "image", "category")
