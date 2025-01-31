from django.contrib import admin
from member_app.models import member, member_config

# Register your models here.
admin.site.register(member)
admin.site.register(member_config)