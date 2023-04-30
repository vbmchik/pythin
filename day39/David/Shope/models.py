from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True) # url ссылка
    
    
    class Meta:
        ordering = ("name", )
        verbose_name = "Категории"
        verbose_name_plural = "Категории" 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Shope:product_list_by_category", args = [self.slug])
     
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True) # url ссылка
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    descreption = models.TextField(blank= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("name",)
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        index_together = ("id", "slug", )
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('Shope:product_detail', args=[self.id, self.slug])
