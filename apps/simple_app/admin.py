from django.contrib import admin
from .models import Messages, Tenant


admin.site.register(Tenant)
admin.site.register(Messages)