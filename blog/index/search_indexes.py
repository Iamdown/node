# -*- coding: utf-8 -*-
'''
File Name:search_indexes.py
Program IDE:PyCharm
Create FIle Time:2022/4/17 13:20
File Create By Author:"祖华"
'''
from .models import Artical
from haystack import indexes
from haystack import indexes
from .models import Artical  # 修改此处，添加自己model


# 类名必须为需要检索的Model_name+Index，这里需要检索Blog，所以创建BlogIndex
class ArticalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

      # 此外可以存在，可以不存在，看具体需要的数据
    """下面这些字段，在索引类中进行申明，在REST framework中，索引类的字段可以被作为索引查询结果返回数据额来源"""
    # id = indexes.IntegerField(model_attr='id')
    # name = indexes.CharField(model_attr='name')
    # price = indexes.DecimalField(model_attr='price')

    """也就是说，前端在索引的时候，可以按照text=xxx,也可以按照id=xxx,name=xxx等，我们的数据返回也是返回id,name,price """

    def get_model(self):
        return Artical  # 添加自己model


    def index_queryset(self, using=None):
        return self.get_model().objects.all()

