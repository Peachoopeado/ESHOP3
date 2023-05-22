from django.db import models

# Create your models here.


class MainPartner(models.Model):
    name = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)
    text = models.TextField(null=True)
    short_video_link = models.CharField(max_length=500)
    long_video_link = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Слайд_Партнёр'
        verbose_name_plural = 'Слайд_Партнёры'
class MainPartnerImg(models.Model):
    partner = models.ForeignKey(MainPartner, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='main/img/partners')

    def __str__(self):
        return self.partner.name
    class Meta:
        verbose_name = 'Слайд_Партнёр_Фото'
        verbose_name_plural = 'Слайд_Партнёры_Фото'

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
class NewsImage(models.Model):
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='main/img/news')

    def __str__(self):
        return self.new.title

    class Meta:
        verbose_name = 'Превью'
        verbose_name_plural = 'Превью'