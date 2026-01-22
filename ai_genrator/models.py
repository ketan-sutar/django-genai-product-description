from django.db import models

# Create your models here.

class ProductDetials(models.Model):
  product_name=models.CharField(max_length=200)
  material=models.CharField(max_length=200)
  color=models.CharField(max_length=100)
  audience=models.CharField(max_length=200)
  description=models.JSONField()
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.product_name