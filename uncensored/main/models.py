from django.db import models
import uuid


# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='thread_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_bump = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-last_bump']

class Reply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    image = models.ImageField(upload_to='reply_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class UUIDModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)



