from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Contact)