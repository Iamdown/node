from django.db import models
# from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     u_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     telephone = models.CharField(max_length=50,blank=True)
#     class Meta:
#         managed = True
#         db_table = 'userprofile'
#
#     def __str__(self):
#         return self.user.username