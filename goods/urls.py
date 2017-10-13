from django.conf.urls import url

from . import views

# urlpatterns是list类型，不是dict类型
urlpatterns = [
    url(r'^$', views.Product, name="products"),
]