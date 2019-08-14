
from company.models import ContactInfo
from products.models import Banner

from apps.utils.concat import Concat
from django.core.exceptions import ObjectDoesNotExist

def get_contactInfo(objs, position, title):
    try:
      return  objs.get(position=position,title=title)
    except ObjectDoesNotExist:
        return ""

top_tel =get_contactInfo(ContactInfo.objects, position=0, title='手机')
top_email = get_contactInfo(ContactInfo.objects, position=0, title='邮件')

side_tel = get_contactInfo(ContactInfo.objects,position=1, title='手机')
side_email = get_contactInfo(ContactInfo.objects,position=1, title='邮件')
other_contacts = ContactInfo.objects.filter(position=2).values('title').annotate(infos=Concat('info'))

other_dicts = {}
for oc in other_contacts:
    key = oc['title']
    value = oc['infos'].replace(',', ' / ')
    other_dicts[key] = value


contact_info = {
    'top_tel': top_tel.info if top_tel != "" else "",
    'top_email': top_email.info if top_email != "" else "",
    'side_tel': side_tel.info if side_tel != "" else "",
    'side_email': side_email.info if side_email != "" else "",
}

contact_info.update({'other_contacts': other_dicts})

all_banners = Banner.objects.all().order_by('index','-add_time')[:5]
contact_info.update({ 'all_banners':all_banners})