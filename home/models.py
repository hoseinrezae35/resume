from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    email = models.EmailField()
    telegram_id = models.CharField(max_length=30, default='https://t.me/hr35o')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/info', null=True, blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='image/portfolio', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactModelForm(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
