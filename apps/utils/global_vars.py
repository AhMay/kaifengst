
from company.models import ContactInfo
from products.models import Banner

from apps.utils.concat import Concat

top_tel = ContactInfo.objects.get(position=0, title='手机')
top_email = ContactInfo.objects.get(position=0, title='邮件')

side_tel = ContactInfo.objects.get(position=1, title='手机')
side_email = ContactInfo.objects.get(position=1, title='邮件')
other_contacts = ContactInfo.objects.filter(position=2).values('title').annotate(infos=Concat('info'))

other_dicts = {}
for oc in other_contacts:
    key = oc['title']
    value = oc['infos'].replace(',', ' / ')
    other_dicts[key] = value


contact_info = {
    'top_tel': top_tel.info,
    'top_email': top_email.info,
    'side_tel': side_tel.info,
    'side_email': side_email.info,
}

contact_info.update({'other_contacts': other_dicts})

all_banners = Banner.objects.all().order_by('index','-add_time')[:5]
contact_info.update({ 'all_banners':all_banners})