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
    code = models.CharField(max_length=100, primary_key=True, default=0, db_index=True)
    vendor_code = models.CharField(max_length=100, unique=True, null = True, blank = True, db_index=True)
    name_m = models.CharField(max_length=200, null=True, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    category = models.ManyToManyField(Category)
    oiltype = models.ForeignKey(OilType,on_delete=models.CASCADE, blank=True , null = True)
    viscosity = models.ForeignKey(Viscosity, on_delete=models.CASCADE, blank=True, null = True)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE, blank=True, null = True)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, blank = True, null = True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default = True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product-detail', args=[self.code])