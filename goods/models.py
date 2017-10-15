from django.db import models

# Create your models here.
class Category(models.Model):
    """
    id	    *类型id
    name	*类型名称
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
    id	        *产品id
    name		*产品名称
    description	*产品描述
    pub_date	*上线日期
    category_id	*类型id
    recommended	*是否推荐商品（0-否，1-是）
    thumbnail1	*缩略图1（保存路径）
    thumbnail2	缩略图1（保存路径）
    thumbnail3	缩略图1（保存路径）
    thumbnail4	缩略图1（保存路径）
    thumbnail5	缩略图1（保存路径）
    carouselIMG	轮播展示图片（保存路径)
    detailIMG1	详情展示图片1（保存路径）
    detailIMG2	详情展示图片2（保存路径）
    detailIMG3	详情展示图片3（保存路径）
    detailIMG4	详情展示图片4（保存路径）
    detailIMG5	详情展示图片5（保存路径）
    detailIMG6	详情展示图片6（保存路径）
    detailIMG7	详情展示图片7（保存路径）
    detailIMG8	详情展示图片8（保存路径）
    detailIMG9	详情展示图片9（保存路径）
    detailIMG10	详情展示图片10（保存路径）
    """
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    pub_date = models.DateTimeField('publish date')
    # TIP: Category定义必须在前面，否则包Category未定义
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recommended = models.BooleanField(default=0)
    thumbnail1 = models.ImageField(upload_to='upload')
    thumbnail2 = models.CharField(max_length=800, default="", blank=True)
    thumbnail3 = models.CharField(max_length=800, default="", blank=True)
    thumbnail4 = models.CharField(max_length=800, default="", blank=True)
    thumbnail5 = models.CharField(max_length=800, default="", blank=True)
    carouselIMG = models.CharField(max_length=800, default="", blank=True)
    detailIMG1 = models.CharField(max_length=800, default="", blank=True)
    detailIMG2 = models.CharField(max_length=800, default="", blank=True)
    detailIMG3 = models.CharField(max_length=800, default="", blank=True)
    detailIMG4 = models.CharField(max_length=800, default="", blank=True)
    detailIMG5 = models.CharField(max_length=800, default="", blank=True)
    detailIMG6 = models.CharField(max_length=800, default="", blank=True)
    detailIMG7 = models.CharField(max_length=800, default="", blank=True)
    detailIMG8 = models.CharField(max_length=800, default="", blank=True)
    detailIMG9 = models.CharField(max_length=800, default="", blank=True)
    detailIMG10 = models.CharField(max_length=800, default="", blank=True)

    def __str__(self):
        return self.name