from django.urls import path
from .views import AddUserAskView, contactus, reply

app_name = 'company'

urlpatterns =[
    path('addask/', AddUserAskView.as_view(), name='add_ask'),
    path('contactus/', contactus, name='contactus'),
    path('reply_ask/<int:askid>/', reply, name='reply_ask'),
]