from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(max_length=100)
    short_description = models.TextField(
        help_text="Short summary for blog listing"
    )

    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
