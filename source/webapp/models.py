from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator, BaseValidator, MaxValueValidator, \
    MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

CATEGORY_CHOICES = [
    ('tech', 'Техника'),
    ('food', 'Еда'),
    ('clothes', 'Одежда')
]
#
# STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
#
#
# @deconstructible
# class MinLengthValidator(BaseValidator):
#     message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
#     code = 'too_short'
#
#     def compare(self, value, limit):
#         return value < limit
#
#     def clean(self, value):
#         return len(value)
#
#
# def at_least_10(string):
#     if len(string) < 10:
#         raise ValidationError('This value is too short!')
#
#
# ##TODO протестировать все валидаторы, понять плюсы и минусы каждого.
#
#
# class TO_DO_List(models.Model):
#     summary = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание',
#                                validators=[MinLengthValidator(10), ])
#     description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание подробное',
#                                    default=None, validators=[at_least_10, ])
#     status = models.ForeignKey('webapp.Statuses', related_name='statuses', on_delete=models.PROTECT,
#                                verbose_name='Статус:')
#     issue = models.ManyToManyField('webapp.Issues', related_name='issueses', blank=False, verbose_name='Тип задачи')
#     project = models.ForeignKey('webapp.Project', related_name='projects', on_delete=models.PROTECT,
#                                 verbose_name='Название проекта:')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
#
#     def __str__(self):
#         return "{}. {}".format(self.pk, self.summary)
#
#
# class Statuses(models.Model):
#     status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус')
#
#     def __str__(self):
#         return self.status
#
#
# class Issues(models.Model):
#     issue = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус')
#
#     def __str__(self):
#         return self.issue
#
#
# class Project(models.Model):
#     begin_date = models.DateField(verbose_name="Дата начала", null=False, blank=False)
#     end_date = models.DateField(verbose_name="Дата  окончания", null=True, blank=True)
#     title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название проекта',
#                              validators=[MinLengthValidator(10), ])
#     description = models.TextField(max_length=3000, null=False, blank=False,verbose_name='Описание проекта',
#                                    validators=[MinLengthValidator(10), ])
#     is_active = models.BooleanField(default=True)
#     team = models.ManyToManyField(get_user_model(), related_name='projects', verbose_name='Команда')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         permissions = {
#             ('can_change_team', 'может редактировать команду преокта')
#         }
# validators=[MinLengthValidator(10), ]


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название проекта', )
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание товара')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return f"{self.title}"

    def get_avg_reviews(self):
        average = 0
        if self.reviews.count():
            for review in self.reviews.all():
                average += review.mark
            average = average / self.reviews.count()
        return round(average, 1)


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='reviews', verbose_name='Отзыв', on_delete=models.CASCADE)
    product = models.ForeignKey('webapp.Product', related_name='reviews', verbose_name='продукт',
                                on_delete=models.CASCADE)
    review = models.TextField(max_length=2000, verbose_name='Описание товара')
    mark = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])