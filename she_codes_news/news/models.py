from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    art_pic = models.ImageField(null=True, blank=True, upload_to='images/')
    


# Add a field to the NewsStory model for an image url 
# and use this image url rather than the default
# images provided in the starter.