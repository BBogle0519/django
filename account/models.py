from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


class MyUserManager(BaseUserManager):
    def create_user(self, user_id, user_nm, user_ph, user_email, password=None):
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = self.model(
            user_id=user_id,
            user_nm=user_nm,
            user_ph=user_ph,
            user_email=self.normalize_email(user_email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_nm, user_ph, user_email, password):
        user = self.create_user(
            user_id=user_id,
            password=password,
            user_nm=user_nm,
            user_ph=user_ph,
            user_email=self.normalize_email(user_email),
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.


class User_Tb(AbstractBaseUser, PermissionsMixin):
    # Field name made lowercase.
    user_id = models.CharField(
        db_column='USER_ID', unique=True, max_length=20, blank=True, null=True)
    # Field name made lowercase.
    user_nm = models.CharField(
        db_column='USER_NM', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    user_ph = models.IntegerField(
        db_column='USER_PH', blank=True, null=True)
    # Field name made lowercase.
    user_email = models.CharField(
        db_column='USER_EMAIL', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    user_reg_ymd = models.DateTimeField(
        db_column='USER_REG_YMD', auto_now_add=True)
    # Field name made lowercase.
    user_st = models.IntegerField(
        db_column='USER_ST', blank=True, null=True, default=1)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_id'

    # 필수로 입력받을 필드 추가
    REQUIRED_FIELDS = ['user_nm', 'user_ph', 'user_email'
    ]

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user_tb'
