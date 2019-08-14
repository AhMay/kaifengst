#company/views.py

import os
from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.views.generic import View

from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from STManager.settings import EMAIL_FROM

from apps.utils.global_vars import contact_info
from .forms import UserAskForm
from .models import UserAsk, AskReply
from products.models import Product,Case

# Create your views here.

@login_required
def reply(request, askid):
    user_ask = UserAsk.objects.get(id=askid)
    mobile = user_ask.mobile
    email = user_ask.email
    asks = UserAsk.objects.filter(Q(mobile=mobile) | Q(email=email)).order_by('due_status', 'add_date') #以手机或邮箱号作为唯一查询
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        method = request.POST.get('method', '')
        ask_id = request.POST.get('askid', '')
        message = request.POST.get('message', '')
        userask = UserAsk.objects.get(id=int(ask_id))
        if method == 'email':
            reply_method = 0;
            email_title = '回复:' + userask.name + "于" + userask.add_date.strftime("%Y-%m-%d %H:%M:%S") + "的留言"
            email_body = message
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [userask.email, EMAIL_FROM])
            # 如果发送成功
            if send_status:
                pass
            else:
                return HttpResponse('{"status":"fail", "msg": "邮件发送失败,请检查用户提供的邮箱是否有非法"}', content_type='application/json')
        elif method == 'save':
            reply_method = 1;

        AskReply.objects.create(message=message, user=request.user, reply_method=reply_method, user_ask=userask)
        userask.due_status = 1
        userask.due_date = datetime.now()
        userask.save()
        return HttpResponse('{"status":"success", "msg": "留言已处理"}', content_type='application/json')
    return render(request, 'reply.html',
                  {
                      'asks': asks,
                  })

def contactus(request):
    return render(request,'contact.html',dict(**contact_info))

class AddUserAskView(View):
    '''用户添加咨询'''
    def post(self, request, *args, **kwargs):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加出错"}', content_type='application/json')

def index(request):
    company_intro = read_company_intro()
    products = Product.objects.all().order_by('-views')[:6]
    hot_cases = Case.objects.all().order_by('-views')[:3]

    return render(request, 'index.html',
                 dict({
                      'company_intro': company_intro,
                      'hots': products,
                     'hot_cases':hot_cases,
                  }, **contact_info))

def read_company_intro():
    file_name = os.path.join('static', 'images', 'company', 'company.txt')
    if not os.path.exists(file_name):
        raise FileNotFoundError(u'公司介绍需要在路径文件中填写{0}'.format(file_name))

    company_intro = ''
    with open(file_name, 'r', encoding='gb2312') as intro:
        company_intro = intro.read()

    return company_intro