from django.db import models
from django.db.models import PROTECT


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField()
    img = models.ImageField(upload_to='')
    category = models.ForeignKey('Category', on_delete=PROTECT, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
