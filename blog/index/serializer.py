# -*- coding: utf-8 -*-
'''
File Name:serializer.py
Program IDE:PyCharm
Create FIle Time:2022/4/18 17:06
File Create By Author:"祖华"
'''
# blog/serializer.py
from .models import *
from .search_indexes import ArticalIndex
from rest_framework.serializers import ModelSerializer
from drf_haystack.serializers import HaystackSerializerMixin


class BlogSerializers(ModelSerializer):
    class Meta:
        model = Artical
        fields = '__all__'


class BlogIndexSerializer(HaystackSerializerMixin, BlogSerializers):
    class Meta(BlogSerializers.Meta):
        index_classes = [ArticalIndex]
        search_fields = ['text', 'a_title', 'a_content']  # 不能和正常搜索一样使用q参数
