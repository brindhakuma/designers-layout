from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='projects/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    old_price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    new_price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hiring_for = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    budget = models.CharField(max_length=100)
    project_description = models.TextField()
    personal_note = models.TextField(blank=True)
    hiring_type = models.CharField(
        max_length=50,
        choices=[('Freelancing', 'Freelancing'), ('Company', 'Company')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hiring_for
