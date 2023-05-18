from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('assortment-by-category', args=[self.slug])


class CategoryImage(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='shop/img/categories')

class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name



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
class Transmission(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)
    oiltype = models.ManyToManyField(OilType)
    viscosity = models.ManyToManyField(Viscosity, blank=True)
    compound = models.ManyToManyField(Compound, blank=True)
    fuel = models.ManyToManyField(Fuel, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=100, primary_key=True, default=0, db_index=True)
    vendor_code = models.CharField(max_length=100, unique=True, null=True, blank=True, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    name_m = models.CharField(max_length=200, null=True, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    visual_name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ManyToManyField(Category)
    oiltype = models.ForeignKey(OilType, on_delete=models.CASCADE, blank=True, null=True, default='-')
    viscosity = models.ManyToManyField(Viscosity, blank=True, null=True, default='-')
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE, blank=True, null=True, default='-')
    fuel = models.ManyToManyField(Fuel, blank=True, default='-')
    transmission = models.ManyToManyField(Transmission, blank=True, default='-')
    volume = models.IntegerField(null=True, blank=True, default='-')
    description = models.TextField(null=True, blank=True, default='-')
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    security_pasport = models.CharField(max_length=300, null=True, blank=True)
    tech_desc = models.CharField(max_length=300, null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    img = ProcessedImageField(upload_to='shop/img/products',
                              processors=[ResizeToFit(245.69, 317.97)],
                              options={'quality': 90},null=True, blank=True)

    def __str__(self):
        return self.code

    def get_url(self):
        return reverse('product-detail', args=[self.code])


class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('one-partner', args=[self.id])



class PartnerImage(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='shop/img/partners')

    def __str__(self):
        return self.partner.name


class User_Request(models.Model):
    full_name = models.CharField('ФИО', max_length=300)
    company = models.CharField('Название организации', max_length=300, blank=True)
    position = models.CharField('Должность', max_length=300, blank=True)
    email = models.EmailField('Почта')
    phone = models.CharField('Номер телефона', max_length=20)
    subject = models.CharField('Тема сообщения', max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
