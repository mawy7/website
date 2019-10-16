from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/',default="blog.jpg")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = AutoSlugField(
        populate_from='title',
        slugify_function=slugify
    )
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)