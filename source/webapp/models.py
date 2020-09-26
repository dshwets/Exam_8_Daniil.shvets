from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator, BaseValidator, MaxValueValidator, \
    MinValueValidator
from django.db import models

CATEGORY_CHOICES = [
    ('tech', 'Техника'),
    ('food', 'Еда'),
    ('clothes', 'Одежда')
]


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
            for review in self.reviews.filter(status=True):
                average += review.mark
            try:
                average = average / self.reviews.filter(status=True).count()
            except ZeroDivisionError:
                average = 0
        return round(average, 1)


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='reviews', verbose_name='Отзыв', on_delete=models.CASCADE)
    product = models.ForeignKey('webapp.Product', related_name='reviews', verbose_name='продукт',
                                on_delete=models.CASCADE)
    review = models.TextField(max_length=2000, verbose_name='Описание товара')
    mark = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    status = models.BooleanField(default=False, verbose_name="Статус")