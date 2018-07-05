#!usr/bin/env python
# -*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name='blog_posts') #ｒｅｌａｔｅｄ——ｎａｍｅ　的作用就是允许类Ｕｓｅｒ反向查询到ＢｌｏｇＡｒｔｉｃｌｅｓ
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 's'

    def __str__(self):
        return self.title


