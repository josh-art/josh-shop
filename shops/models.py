from django.db import models
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=15, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops:product_detail', args=[self.id, self.slug])



class Contacts(models.Model):
    user_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=100)
    submitted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.user_name

    pass



# Create your models here.
