from django.urls import path

from shop import views

urlpatterns = [
    path("", views.BaseHomePageView.as_view(), name="home_page"),
    path("create-product/", views.CreateGoodsView.as_view(), name="create_page"),
]
