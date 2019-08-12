from datetime import datetime
from django.db import models
from django.core.exceptions import FieldError

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class ContactInfo(models.Model):
    POSITION_CHOICES=(
        (0, '顶部'),
        (1, '边上'),
        (2, '其他'),
    )
    title = models.CharField('名称', max_length=20, blank=True, default='')
    info = models.CharField('联系信息', max_length=50)
    position = models.SmallIntegerField(verbose_name='位置', choices=POSITION_CHOICES, default=2)

    class Meta:
        verbose_name = '联系信息'
        verbose_name_plural = verbose_name
        unique_together = ('title', 'info', 'position')

    def __str__(self):
        return '{}{}'.format(self.title,self.info)

    def save(self, *args, **kwargs):
        '''顶部联系方式和边上联系方式 只能定义一个实例'''
        if self.position in (0,1):
            if self.title not in ('手机', '邮件'):
                raise FieldError('如果要定义 顶部或边上的联系方式，名称只能是 "手机" 或 "邮件" ')
            exist_obj = ContactInfo.objects.filter(position=self.position, title=self.title)
            if exist_obj:
                exist_obj.delete()
        super().save(*args, **kwargs)

class UserAsk(models.Model):
    '''用户咨询'''
    MESSAGE_STATUS_CHOICES=(
        (0, '未处理'),
        (1, '已处理'),
    )
    name = models.CharField('姓名', max_length=20)
    mobile = models.CharField('手机', max_length=11, blank=True)
    message = models.CharField('消息内容', max_length=500)
    email = models.EmailField('邮箱', max_length=50)
    add_date = models.DateTimeField('咨询时间',auto_now=True)
    due_date = models.DateTimeField('回复时间', blank=True, null=True)
    due_status = models.SmallIntegerField(verbose_name='咨询处理状态', choices=MESSAGE_STATUS_CHOICES, default=0)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def go_to(self):
        from django.utils.safestring import mark_safe
        # mark_safe后就不会转义
        url = reverse('company:reply_ask', kwargs={'askid': self.id})
        return mark_safe("<a href='" + url + "' target='_blank'>去处理</a>")

    go_to.short_description = "去处理"

class AskReply(models.Model):
    REPLY_CHOICES =(
        (0, '邮件'),
        (1, '非邮件'),
    )
    message = models.CharField('回复消息', max_length=500)
    user = models.ForeignKey(User, verbose_name='回复人', on_delete=models.SET_NULL, null=True)
    reply_method = models.SmallIntegerField(verbose_name='回复方式', choices=REPLY_CHOICES, default=0)
    user_ask = models.ForeignKey(UserAsk, verbose_name='用户咨询', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '留言回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '回复{}的留言'.format(self.user_ask.name)