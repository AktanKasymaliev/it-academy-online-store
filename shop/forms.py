from django import forms

from .models import ShopGoods


class GoodsCreateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ShopGoods
        fields = ("title", "description", "price", "image", "category", "from_at")
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text area'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            "category": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            # "image": forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            "from_at": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'From at'})
        }
