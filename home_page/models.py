from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    text = models.TextField()


class Langueges(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatar')
    fullname = models.CharField(max_length=150)
    about_me = models.TextField()
    biography = models.TextField()
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    langueges = models.ManyToManyField(Langueges)
    nationality = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    linkedin = models.URLField(null=True, blank=True)
    skype = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)


class Degrees(models.Model):
    university_name = models.CharField(max_length=150)
    education_degree = models.CharField(max_length=150, null=True)
    education_times = models.CharField(max_length=15)
    education_field = models.CharField(max_length=100)
    about_degree = models.TextField(null=True, blank=True)


class Experiences(models.Model):
    office_name = models.CharField(max_length=150)
    work_times = models.CharField(max_length=15)
    work_field = models.CharField(max_length=100)
    about_office = models.TextField(null=True, blank=True)


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    knowledge_percent_skill = models.IntegerField()


class Services(models.Model):
    service_title = models.CharField(max_length=100)
    about_service = models.TextField()
    start_price = models.IntegerField(null=True, blank=True)


class Portfolio(models.Model):
    project_url = models.URLField()
    project_title = models.CharField(max_length=100)
    project_source = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='images/project_images')


class Clients(models.Model):
    client_image = models.ImageField(upload_to='images/clients_image')
    client_site_url = models.URLField()
    client_name = models.CharField(max_length=150, null=True)
