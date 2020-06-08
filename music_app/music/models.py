from django.db import models
from django.utils.text import slugify
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Author(models.Model):
    first_name  = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email = models.EmailField()
    # date  = models.DateField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    


class Post(models.Model):
    title           = models.CharField(max_length=50, blank=True, null=True)
    description     = models.TextField(max_length=500)
    body            = models.TextField(default='')
    video_url       = models.URLField(max_length=500, blank=True)
    slug            = models.SlugField(default='', blank=True, max_length=40, unique=True)
    image           = models.ImageField(upload_to='post_images')
    date            = models.DateField(auto_now=True)
    author          = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_thumbnail = ImageSpecField(source='image',
                                        processors=[ResizeToFill(1332, 850)],
                                        format='JPEG',
                                        options={'quality': 70})
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['id']
        
class InfoSource(models.Model):
    info_source = models.URLField()        
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class WordsOfWisdom(models.Model):
    title       = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='wisdom_images', default="scoan.png")
    contents    = models.TextField()
    date        = models.DateField(auto_now=True)
    image_thumbnail = ImageSpecField(source='image',
                                        processors=[ResizeToFill(1332, 850)],
                                        format='JPEG',
                                        options={'quality': 70})
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

class AboutMe(models.Model):
    intro       = models.TextField()        
    work        = models.TextField(default="", null=True)
    accomplish  = models.TextField()
    date        = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.intro

class Experience(models.Model):
    header = models.CharField(max_length=500)   
    contents = models.TextField() 
    myExperience        = models.ForeignKey(AboutMe, on_delete=models.CASCADE)

    def __str__(self):
        return self.header
    