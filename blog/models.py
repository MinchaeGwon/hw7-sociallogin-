from django.db import models
from imagekit.models import ImageSpecField #이 함수로 썸네일 만듦
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="images/")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':60})
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]