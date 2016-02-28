from django.db import models
from django.utils import html



# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length =50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class Video(models.Model):

    CASE_STUDY = 'CS'
    LESSON = 'L'
    PROMO = 'P'

    CategoryChoices = (
        (CASE_STUDY, 'Case Study'),
        (LESSON, 'Lesson'),
        (PROMO, 'Promo')
    )

    title = models.CharField(max_length = 200)
    description = models.TextField()
    priority = models.SmallIntegerField()
    roles = models.ManyToManyField(Role)
    company = models.ForeignKey('Company')
    hidden = models.BooleanField()
    slug = models.SlugField(unique=True)
    key = models.IntegerField(unique=True)
    category = models.CharField(max_length=2, choices = CategoryChoices, default = LESSON)


    def __str__(self):
        return self.title

    @staticmethod
    def getSmallerSize(devisor):
        largest_width = 1280
        largest_height = 720
        width = str(largest_width/devisor)
        height = str(largest_height/devisor)        
        return (width,height)

    @classmethod
    def getVideos(self,includeHidden=False, **params):
        return self.objects.filter(hidden=includeHidden, **params)









