from pyexpat import model
from tkinter import CASCADE
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'drinks'

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allegy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allegy'

class Allegy_drink(models.Model):
    allegy = models.ForeignKey('Allegy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allegy_drink'

class Size(models.Model):
    name = models.CharField(max_length=20)
    size_mi = models.CharField(max_length=20)
    size_fluid_ounce = models.CharField(max_length=20)

    class Meta:
        db_table = 'sizes'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(decimal_places=2, max_digits=10)
    sodium_mg = models.DecimalField(decimal_places=2, max_digits=10)
    saturated_fat = models.DecimalField(decimal_places=2, max_digits=10)
    sugars_g = models.DecimalField(decimal_places=2, max_digits=10)
    protein_g = models.DecimalField(decimal_places=2, max_digits=10)
    caffeine_mg = models.DecimalField(decimal_places=2, max_digits=10)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'