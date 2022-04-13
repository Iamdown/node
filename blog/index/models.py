# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#from user.models import UserProfile
from mdeditor.fields import MDTextField
from django.contrib.auth import settings


class Topic(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=15,null=False,blank=False)
    class Meta:
        managed = True
        db_table = 'topic'
       # verbose_name_plural = '主题'
    def __str__(self):
        return self.t_name


class Categroy(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50,null=False,blank=False)
    topic = models.ForeignKey("Topic",on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'categroy'
        #verbose_name_plural = '类别'
    def __str__(self):
        return self.c_name




class Artical(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_title = models.CharField(max_length=300,null=False,blank=False)
    a_auth_name = models.CharField(max_length=50,null=True,blank=True,default='无名')
    a_publish_date = models.DateField(null=False,blank=False)
    a_publish_time = models.TimeField(null=False,blank=False)
    #a_content = models.TextField(null=True,blank=True)
    a_content = MDTextField(verbose_name='文章内容',default='')
    category = models.ForeignKey("Categroy",on_delete=models.CASCADE)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'artical'
        #verbose_name_plural = '文章'
        ordering = ["-a_publish_date",'-a_id']

    def __str__(self):
        return self.a_title


class Comment(models.Model):  # 定义评论模型

    comment_content = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey("Artical", on_delete=models.DO_NOTHING, verbose_name='评论文章')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='评论者')
    pre_comment = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,verbose_name='父评论id')  # 父级评论，如果没有父级则为空NULL, "self"表示外键关联自己
    unique_code = models.CharField(max_length=36,unique=True, null=True, verbose_name="唯一识别码")
    level = models.IntegerField(verbose_name="Level",null=True)
    like = models.IntegerField(verbose_name="Like",null=True)
    love = models.IntegerField(verbose_name="Love",null=True)
    care = models.IntegerField(verbose_name="Care",null=True)
    haha = models.IntegerField(verbose_name="Haha",null=True)
    angry = models.IntegerField(verbose_name="Angry",null=True)
    wow = models.IntegerField(verbose_name="Wow",null=True)
    sad = models.IntegerField(verbose_name="Sad",null=True)

    class Meta:
        db_table = 'comment'
       # verbose_name = '评论'
        verbose_name_plural = "comment"
        ordering = ['-comment_time']

    def __str__(self):
        return self.comment_content




