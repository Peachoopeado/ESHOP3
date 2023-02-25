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
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    oiltype = models.ForeignKey(OilType,on_delete=models.CASCADE, blank=True)
    viscosity = models.ForeignKey(Viscosity, on_delete=models.CASCADE, blank=True)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE, blank=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default = True)

    def __str__(self):
        return self.name
