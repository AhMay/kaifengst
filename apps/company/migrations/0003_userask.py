# Generated by Django 2.2.3 on 2019-08-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190803_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(blank=True, max_length=11, verbose_name='手机')),
                ('message', models.CharField(max_length=500, verbose_name='消息内容')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户咨询',
                'verbose_name_plural': '用户咨询',
            },
        ),
    ]
