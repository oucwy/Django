# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# markwy
# 2021.6/4 

class Student (models.Model):
    GENDER_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (1, '通过'),
        (2, '拒绝'),
        (0, '申请'),
    ]
    name = models.CharField(max_length=40, verbose_name="姓名")
    gender = models.IntegerField(choices=GENDER_ITEMS, default=0, verbose_name="性别")
    phone = models.CharField(max_length=20, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    """
    classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
    可以来调用类的属性，类的方法，实例化对象等。
    """
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"
