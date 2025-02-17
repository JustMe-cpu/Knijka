from django.db import models
class Book(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name