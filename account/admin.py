from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseMemberAdmin
from .models import User_Tb

# Register your models here.
class Myadmin(BaseMemberAdmin):
    list_display = ('user_id', 'user_nm', 'user_ph',
                    'user_email', 'user_reg_ymd',)
    list_filter = ()
    search_fields = ('user_id',)
    filter_horizontal = ()
    ordering = ('-user_reg_ymd',)


admin.site.register(User_Tb, Myadmin)
admin.site.unregister(Group)
