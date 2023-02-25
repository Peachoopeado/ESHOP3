from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('assortment-by-category', args=[self.slug])

class OilType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name




class Viscosity(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)
    oiltype = models.ManyToManyField(OilType)

    def __str__(self):
        return self.name


class Compound(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)
    oiltype = models.ManyToManyField(OilType)
    viscosity = models.ManyToManyField(Viscosity)

    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)
    oiltype = models.ManyToManyField(OilType)
    viscosity = models.ManyToManyField(Viscosity)
    compound = models.ManyToManyField(Compound)

    def __str__(self):
        return self.name