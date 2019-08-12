import xadmin

from .models import ContactInfo, UserAsk

class ContactInfoAdmin(object):
    '''关键字'''
    #显示的列
    list_display = ['position', 'title', 'info']
    #搜索的字段
    search_fields = ['title', 'info']
    #过滤
    list_filter = ['title', 'info']

xadmin.site.register(ContactInfo, ContactInfoAdmin)

class UserAskAdmin(object):
    '''关键字'''
    #显示的列
    list_display = ['name', 'mobile', 'message', 'email', 'add_date', 'due_status', 'due_date', 'go_to']
    #搜索的字段
    search_fields = ['name', 'email']
    #过滤
    list_filter = ['name', 'mobile', 'message','email']

xadmin.site.register(UserAsk, UserAskAdmin)