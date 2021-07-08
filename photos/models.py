from django.db import models
from django.urls import reverse


class Post(models.Model):
    uploaded_by = models.CharField(max_length=400)
    image_file = models.ImageField(verbose_name='Pic', upload_to='photos/')
    caption = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Post by {}".format(self.uploaded_by)

    def get_clean_time(self):
        return self.time.strftime("%B %d, %Y, %I:%M %p")

    def liking_url(self):
        return reverse('photos:liker', args=[str(self.pk)])

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        return super().delete()
