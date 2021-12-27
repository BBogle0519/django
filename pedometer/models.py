from django.db import models

# Create your models here.


class stepCount(models.Model):
    step = models.IntegerField(null=True, default=0)
    record = models.DateTimeField(auto_now_add=True, null=False)
    user_id = models.ForeignKey(
        'account.User_Tb', db_column='user_id', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'stepCount'
