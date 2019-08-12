# Generated by Django 2.2.3 on 2019-08-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='position',
            field=models.SmallIntegerField(choices=[(0, '顶部'), (1, '边上'), (2, '其他')], default=2, verbose_name='位置'),
        ),
        migrations.AlterUniqueTogether(
            name='contactinfo',
            unique_together={('title', 'info', 'position')},
        ),
    ]
