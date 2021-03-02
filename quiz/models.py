from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(to='Category', related_name='quizzes', on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.title


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    ]

    TYPE_CHOICES = [
        (0, _('Multiple Choice'))
    ]

    title = models.CharField(max_length=250)
    quiz = models.ForeignKey(to='Quiz', related_name='questions', on_delete=models.CASCADE)
    question_type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=0)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    question = models.ForeignKey(to='Question', related_name='options', on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
