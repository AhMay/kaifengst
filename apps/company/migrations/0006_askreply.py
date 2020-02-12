# Generated by Django 2.2.3 on 2019-08-06 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0005_auto_20190805_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, verbose_name='回复消息')),
                ('reply_method', models.SmallIntegerField(choices=[(0, '邮件'), (1, '非邮件')], default=0, verbose_name='回复方式')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='回复人')),
                ('user_ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.UserAsk', verbose_name='用户咨询')),
            ],
            options={
                'verbose_name': '留言回复',
                'verbose_name_plural': '留言回复',
            },
        ),
    ]