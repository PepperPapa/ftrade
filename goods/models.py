from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')
    # TIP: Category定义必须在前面，否则包Category未定义
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name