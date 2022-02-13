from django.contrib import admin

from .models import User, Profile, Blood

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Blood)
# Register your models here.
