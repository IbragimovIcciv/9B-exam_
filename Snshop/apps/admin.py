from django.contrib import admin
from .models import Users, Phone, Homepage, Aboutpage, conatact_us

admin.site.register(Users)
admin.site.register(Phone)
admin.site.register(Homepage)
admin.site.register(Aboutpage)

admin.site.register(conatact_us)