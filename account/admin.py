from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseMemberAdmin
from .forms import MemberChangeForm, MemberCreationForm
from .models import User_Tb

# Register your models here.


class Myadmin(BaseMemberAdmin):
    # form = MemberChangeForm
    # add_form = MemberCreationForm

    list_display = ('id', 'password', 'user_id', 'user_nm', 'user_ph','user_sex', 'user_tall',
                    'user_email', 'user_reg_ymd', 'user_st',)
    list_filter = ()
    search_fields = ('user_id',)

    # admin 페이지에서 사용자 수정할때 입력폼
    # fieldsets = (
    #     (None, {'fields': ('user_id', 'password')}),
    #     ('Personal info', {'fields': ('user_nm', 'user_ph', 'user_email',
    #                                   'user_reg_ymd',)}),
    #     ('Permissions', {'fields': ('user_st',)}),
    # )

    # admin 페이지에서 사용자 추가할때 입력폼
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('user_id', 'password', 'user_nm',
    #                    'user_ph', 'user_email',
    #                    )
    #     }
    #     ),
    # )

    filter_horizontal = ()
    ordering = ('-user_reg_ymd',)


admin.site.register(User_Tb, Myadmin)
admin.site.unregister(Group)
