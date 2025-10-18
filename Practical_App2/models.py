from django.db import models

class saleModel(models.Model):
    Product_Name = models.CharField(max_length=200, null=True, ) 
    Catagory = models.CharField(max_length=100, null=True,) 
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank=True)
    sale_date = models.DateField( )
    
    
    
    