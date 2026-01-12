from django.db import models
from django.contrib.auth.models import User

class ScrollImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products//')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ScrollImage {self.id}"
