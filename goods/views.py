from django.shortcuts import get_object_or_404, render

from .models import Category, Goods
# Create your views here.
def index(request):
    all_goods_list = Goods.objects.order_by("-pub_date")
    context = {
        'all_goods_list': all_goods_list,
        'recommend_goods_1': all_goods_list[0],
        'recommend_goods_2': all_goods_list[1],
        'recommend_goods_3': all_goods_list[2],
    }
    return render(request, 'goods/index.html', context)

def detail(request, goods_id):
    offer = get_object_or_404(Goods, pk=goods_id)
    offer_category = get_object_or_404(Category, pk=offer.category_id)
    offer_detail = {
        'offer': offer,
        'category': offer_category
    }
    return render(request, 'goods/detail.html', offer_detail)