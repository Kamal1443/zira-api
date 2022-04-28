from django.db import models

# Create your models here.

class Receipt(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.title

        