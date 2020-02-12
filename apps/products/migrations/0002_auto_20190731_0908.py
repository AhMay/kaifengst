# Generated by Django 2.2.3 on 2019-07-31 09:08

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '产品类别', 'verbose_name_plural': '产品类别'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': '产品关键字', 'verbose_name_plural': '产品关键字'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品', 'verbose_name_plural': '产品'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='view',
            new_name='views',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='产品描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/default.jpg', upload_to=products.models.path_and_rename, verbose_name='封面图'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y%m', verbose_name='轮播图')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]