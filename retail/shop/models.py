from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True)
    
    #def get_absolute_url(self):
    #    return reverse('shop:product_list', args=[self.slug])
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'категории'
        verbose_name_plural = 'Категории'
        
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    #def get_absolute_url(self):
    #    return reverse('shop:product_list', args=[self.id, self.slug])
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'продукты'
        verbose_name_plural = 'Продукты'
        
    def __str__(self) -> str:
        return self.name
