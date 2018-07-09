from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
class Course(models.Model):
    
    owner = models.ForeignKey(User,
                              related_name='courses_created',null=True,blank=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject,
                              related_name='subject',null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User,
                                      related_name='courses_joined',
                                      blank=True)
    
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules',null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])
    
    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents',null=True,blank=True,on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType,on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id', )
    content_type = models.ForeignKey(ContentType,
                            on_delete=models.SET_NULL,
                            limit_choices_to={'model__in':('text',
                                            'video',
                                            'image',
                                            'file' )})
    order = OrderField(blank = True, for_fields=['module'])

    class Meta:
        ordering = ['order']                                        

class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def render(self):
        return render_to_string('courses/content/{}.html'.format(
                self._meta.model_name), {'item': self})
            
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
class Text(ItemBase):
    content = models.TextField()
class File(ItemBase):
    file = models.FileField(upload_to='files')
class Image(ItemBase):
        file = models.FileField(upload_to='images',)
class Video(ItemBase):
    url = models.URLField()


