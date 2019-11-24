from django.db import models

# Create your models here.
class PantryItem(models.Model):
    image = models.ImageField(upload_to='foodpantry/images/', default='images/noimage.png')
    name = models.CharField(max_length=64)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.points} points)"

