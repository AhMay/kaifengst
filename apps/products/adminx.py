import xadmin
from xadmin import views

from .models import Category, KeyWord, Product, Banner, Case

class CaseAdmin(object):
    '''技术支持'''
    #显示的列
    list_display = ['title',  'author', 'views', 'keywords', 'add_date']
    #搜索的字段
    search_fields = ['title', 'author', ]
    #过滤
    list_filter = ['title', 'author', 'views', 'keywords', 'add_date']

    style_fields = {"desc": "ueditor"}

xadmin.site.register(Case, CaseAdmin)

class CategoryAdmin(object):
    '''类别'''
    #显示的列
    list_display = ['name']
    #搜索的字段
    search_fields = ['name']
    #过滤
    list_filter = ['name']

xadmin.site.register(Category, CategoryAdmin)

class KeyWordAdmin(object):
    '''关键字'''
    #显示的列
    list_display = ['name']
    #搜索的字段
    search_fields = ['name']
    #过滤
    list_filter = ['name']

xadmin.site.register(KeyWord, KeyWordAdmin)

class ProductAdmin(object):
    '''产品'''
    #显示的列
    list_display = ['category', 'name', 'author', 'views', 'add_date', 'keywords']
    #搜索的字段
    search_fields = ['category__name', 'name', 'author', 'keywords']
    #过滤
    list_filter = ['category', 'name', 'author', 'keywords']

    style_fields = {"desc": "ueditor"}

xadmin.site.register(Product, ProductAdmin)

class BannerAdmin(object):
    '''轮播图'''
    #显示的列
    list_display = ['title', 'index', 'image', 'add_time']
    #搜索的字段
    search_fields = ['title', 'index']
    #过滤
    list_filter = [ 'title']

xadmin.site.register(Banner, BannerAdmin)


# xadmin 的基本管理器配置
class BaseSetting(object):
    #开启主题功能
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    #修改 title
    site_title = "开封宋通轴承有限责任公司后台"
    # 修改footer
    site_footer = 'ST'
    #收起菜单
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSettings)

