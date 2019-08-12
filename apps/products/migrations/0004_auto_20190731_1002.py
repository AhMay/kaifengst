# Generated by Django 2.2.3 on 2019-07-31 10:02

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190731_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/default.jpg', null=True, upload_to=products.models.path_and_rename, verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='products.KeyWord', verbose_name='关键字'),
        ),
    ]
