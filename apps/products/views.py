from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Category, Product, Case

from apps.utils.global_vars import contact_info

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    paginate_by = 6

    def get_queryset(self):
        category_id = self.request.GET.get('ct', '')
        objs = Product.objects.all().order_by('-views')
        if category_id != '':
            objs = objs.filter(category__id=int(category_id))
        # 搜索功能
        search_keywords = self.request.GET.get('keywords', '')  # 搜索
        search_type = self.request.GET.get('type', '')
        if search_keywords:
            if search_type == 'category': # 类别只能选一个
                categories =  Category.objects.filter(name__icontains=search_keywords)
                if categories:
                    objs = Product.objects.filter(category__in=categories)
            elif search_type == 'product':
                objs = Product.objects.filter(Q(name__icontains=search_keywords) |
                                              Q(desc__icontains=search_keywords))
        return objs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        search_keywords = self.request.GET.get('keywords', '')  # 搜索
        search_type = self.request.GET.get('type', '')
        if search_type:
            if search_type == 'category':
                context['categories'] = Category.objects.filter(name__icontains=search_keywords)
            context['keywords'] = search_keywords
            context['type'] = search_type

        context['hots'] = Product.objects.all().order_by('-views')[:3]
        context['cur_category'] ='全部产品'
        category_id = self.request.GET.get('ct', '')
        if category_id != '':
            context['cur_category'] = Category.objects.get(id=int(category_id)).name
        return dict(context, **contact_info)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.viewed()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hots'] = Product.objects.all().order_by('-views')[:3]
        all_category_products = Product.objects.filter(category_id=context['product'].category.id).order_by('id')
        context['pre_product'] = all_category_products.filter(id__lt=context['product'].id).first()
        context['next_product'] = all_category_products.filter(id__gt=context['product'].id).first()

        return dict(context,**contact_info)

class CaseListView(ListView):
    model = Case
    template_name = "cases.html"
    paginate_by = 20

    def get_queryset(self):
        objs = Case.objects.all().order_by('-views', '-add_date')
        # 搜索功能
        search_keywords = self.request.GET.get('keywords', '')  # 搜索
        search_type = self.request.GET.get('type', '')
        if search_keywords:
            if search_type == 'case':
               objs = objs.filter(Q(title__icontains=search_keywords) |
                                          Q(desc__icontains=search_keywords))
        return objs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hots'] = Product.objects.all().order_by('-views')[:3]
        search_keywords = self.request.GET.get('keywords', '')  # 搜索
        search_type = self.request.GET.get('type', '')
        if search_keywords:
            context['keywords'] = search_keywords
            context['type'] = search_type
        return dict(context,**contact_info)

class CaseDetailView(DetailView):
    model = Case
    template_name = 'case.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.viewed()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hots'] = Product.objects.all().order_by('-views')[:3]
        cases = Case.objects.all()
        context['pre_case'] = cases.filter(id__lt=context['case'].id).first()
        context['next_case'] = cases.filter(id__gt=context['case'].id).first()
        print(context['pre_case'])
        print(context['next_case'])
        return dict(context,**contact_info)