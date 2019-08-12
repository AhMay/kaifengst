import os
from datetime import datetime
import uuid

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Category(models.Model):
    '''产品类别'''
    name = models.CharField(max_length=30, verbose_name='产品类别', unique=True)

    class Meta:
        verbose_name = "产品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class KeyWord(models.Model):
    '''产品关键字'''
    name = models.CharField(max_length=10, verbose_name='关键字')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品关键字"
        verbose_name_plural = verbose_name

def path_and_rename(instance, filename):
    upload_to = 'products'
    ext = filename.split('.')[-1].lower()
    if ext not in ['jpg', 'png', 'gif']:
        raise models.FieldError('we only support .jpg and .png imge')
    filename = "{}.{}".format(uuid.uuid4().hex[:10], ext)
    return os.path.join(upload_to, filename)

class Product(models.Model):
    '''产品'''
    category = models.ForeignKey(Category, verbose_name='所属类别', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='产品名')
    #desc = models.TextField(verbose_name='产品描述')
    brief = models.CharField(verbose_name='简单描述', default='', max_length=100)
    desc = UEditorField(verbose_name=u'产品描述', width=600, height=300, imagePath="products/ueditor/",
                          filePath="products/ueditor/", default='')
    image = models.ImageField(verbose_name='封面图', upload_to=path_and_rename, default='products/default.jpg', blank=True, null=True)
    author = models.CharField(verbose_name='作者', max_length=20, default=u'宋通轴承')
    views = models.PositiveIntegerField(verbose_name='热度', default=0)
    add_date = models.DateField(verbose_name='日期', auto_now_add=True)
    keywords = models.ManyToManyField(KeyWord, verbose_name='关键字', blank=True, null=True)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    '''轮播图'''
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m', max_length=100)  # /media/banner/xx
    index = models.IntegerField('顺序', default=100)  # 控制轮播顺序
    product = models.ForeignKey(Product, verbose_name='产品', on_delete=models.CASCADE) #首页可以访问的产品
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

class Case(models.Model):
    '''技术支持'''
    title = models.CharField(max_length=50, verbose_name='文章名')
    brief = models.CharField(verbose_name='简单描述', default='', max_length=100)
    desc = UEditorField(verbose_name=u'文章内容', width=600, height=300, imagePath="supports/ueditor/",
                        filePath="supports/ueditor/", default='')
    author = models.CharField(verbose_name='作者', max_length=20, default=u'宋通轴承')
    views = models.PositiveIntegerField(verbose_name='热度', default=0)
    add_date = models.DateField(verbose_name='日期', auto_now_add=True)
    keywords = models.ManyToManyField(KeyWord, verbose_name='关键字', blank=True, null=True)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "技术支持"
        verbose_name_plural = verbose_name