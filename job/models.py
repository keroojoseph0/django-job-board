from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE = [
    ("full time", "full time"),
    ("part time", "part time")
]

def image_upload(instance, filename):
    imagenmae, extension = filename.split('.')
    return f"jobs/{instance.id}.{extension}"

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null= True, blank= True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
