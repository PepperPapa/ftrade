from django.conf.urls import url

from . import views

# urlpatterns是list类型，不是dict类型
urlpatterns = [
    # /goods/
    url(r'^$', views.index, name="index"),
    # /goods/detail/
    url(r'^(?P<goods_id>[0-9]+)/$', views.detail, name="detail")
]