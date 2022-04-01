"""..."""
from django.db import models


class Category(models.Model):
    """..."""
    name = models.CharField(max_length=20)


class User(models.Model):
    """..."""


class Answer(models.Model):
    """..."""
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True)


class Question(models.Model):
    """..."""
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='questions',
                               null=True)
    answer = models.OneToOneField(Answer,
                                  on_delete=models.SET_NULL,
                                  related_name='question',
                                  null=True)
    category = models.ManyToManyField(Category)


class Comment(models.Model):
    """..."""
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='comments',
                               null=True)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
