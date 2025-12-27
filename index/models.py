from django.db import models

# Create your models here.

class Punt_tonal(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True) 
    
    def __str__(self):
        return self.name
    
    
class Punet_qe_bejm(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/', null=True, blank=True) 
    
    def __str__(self):
        return self.name
    
