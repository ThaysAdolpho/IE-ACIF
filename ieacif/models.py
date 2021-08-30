from django.db import models

class Home(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True, upload_to="imagem/%Y/%m/%D/")

    def __str__(self):
        return self.title