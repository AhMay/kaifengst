# Generated by Django 2.2.3 on 2019-07-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190731_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='产品类别'),
        ),
    ]