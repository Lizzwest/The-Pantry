from django.db import models
from django.contrib.auth.models import User



# Create your models here.
CATEGORY_CHOICES = (
    ('grain','GRAIN'),
    ('vegetables', 'VEGETABLES'),
    ('fruits','FRUITS'),
    ('dairy','DAIRY'),
    ('meat','MEAT'),
    ('misc','MISCELLANEOUS')
)
# Create your models here.
class Post(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='grain')
    itemName = models.CharField(max_length=100)
    weightQuantity = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemName