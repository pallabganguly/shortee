from django.db import models
from django.conf import settings
from .validators import validate_url

# Create your models here.
# handles and manipulates data for database
# manipulates and handles stuff related to the models

from .utils import code_generator, create_shortcode

MAX_SHORTCODE = getattr(settings, 'MAX_SHORTCODE', 16)# same as MAX_SHORTCODE = settings.MAX_SHORTCODE

# to show overriding methods in Models Managers like all, count, filter.
class UrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qsinit = super().all(*args, **kwargs)
        # print(qsinit)
        qs = qsinit.filter(active=True)
        return qs

    def refresh_all_shortcodes(self):
        qset = UrlShort.objects.filter(id__gte=1) # filter bu id >= 1
        count = 0
        for query in qset:
            query.short = None
            query.save()
            count += 1
        return str(count)+' records changed'

class UrlShort(models.Model):
    url = models.CharField(max_length = 255, validators=[validate_url])
    shortcode = models.CharField(max_length = MAX_SHORTCODE, unique = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)

    objects = UrlManager()

    # overrides the defaul save method in models. Specifies what to do when new onject is saved to database
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return "http://www.shortee.com:5000/{scode}".format(scode=self.shortcode)


'''
    after changing this file run python manage.py makemigrations
    followed by python manage.py migrate
'''
