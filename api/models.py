from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from api.options import category
# Get generic User
User = get_user_model()

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, 
                               on_delete=models.SET_NULL,
                                null=True)

    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)
    category = models.CharField(choices = category, max_length=25)

    content = models.TextField()
    img_url = models.CharField(max_length = 225, 
                               default = 'istockphoto.com/beards.jpg')

    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f'{self.slug}'
    
    class Meta:
        ordering = ['-created_at']
