from django.shortcuts import redirect
from django.views import generic

from .forms import GoodsCreateForm
from .models import ShopGoods


class BaseHomePageView(generic.ListView):
    template_name = "shop/shop_page.html"
    queryset = ShopGoods.objects.all()


class CreateGoodsView(generic.CreateView):
    template_name = "shop/product_create.html"
    queryset = ShopGoods.objects.all()
    form_class = GoodsCreateForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect("home_page")
