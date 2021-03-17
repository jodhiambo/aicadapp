from django.db import models
from django.utils import timezone
import datetime
from PIL import Image
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


TAGS = (
    ('ALL', 'ALL'),
    ('AGRICULTURE', 'AGRICULTURE'),
    ('TRAINING', 'TRAINING'),
    ('TECHNOLOGY', 'TECHNOLOGY'),


)

class Project(models.Model):
    tags = MultiSelectField(choices=TAGS, max_length=120, max_choices=2, default='ALL')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, default=None)
    benefitiary = models.CharField(max_length=150)
    description = models.TextField()
    location = models.TextField()
    point_of_contact = models.TextField()
    date = models.DateTimeField(default=timezone.now, db_index=True)
    status = models.CharField(max_length=150)


    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    post = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media_pics/%Y/%m/%d')

    def __str__(self):
        return self.post.title

class Patner(models.Model):
    image = models.ImageField(blank=True, default=None)
    external_url = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.external_url

class Advert(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    pdf = models.FileField(upload_to='pdf/%Y/%m/%d')

    def __str__(self):
        return self.title
