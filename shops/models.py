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
    slug = models.SlugField(max_length=20, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops:product_detail', args=[self.id, self.slug])


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    sale_price = models.DecimalField(
        decimal_places=2, max_digits=20, null=True, blank=True)
    DEFAULT = 'DEFAULT'
    RED = 'RED'
    BLUE = 'BLUE'
    YELLOW = 'YELLOW'
    ORANGE = 'ORANGE'
    GREEN = 'GREEN'
    PINK = 'PINK'
    BLACK = 'BLACK'
    WHITE = 'WHITE'
    GREY = 'GREY'
    TYP = (
        (DEFAULT, 'DEFAULT'),
        (RED, 'RED'),
        (BLUE, 'BLUE'),
        (YELLOW, 'YELLOW'),
        (ORANGE, 'ORANGE'),
        (GREEN, 'GREEN'),
        (PINK, 'PINK'),
        (BLACK, 'BLACK'),
        (WHITE, 'WHITE'),
        (GREY, 'GREY')
    )
    color = models.CharField(max_length=100, choices=TYP, default=DEFAULT)
    NA = 'N/A'
    UNISEX = 'Unisex'
    MALE = 'Male'
    FEMALE = 'N/A'
    FEMALE = 'Female'
    TYP = (
        (NA, 'N/A'),
        (UNISEX, 'Unisex'),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(max_length=10, choices=TYP, default=UNISEX)
    NA = 'N/A'
    CHILDREN = 'Children'
    ADULT = 'Adult'
    TYP = (
        (NA, 'N/A'),
        (CHILDREN, 'Children'),
        (ADULT, 'Adult')
    )
    age = models.CharField(max_length=10, choices=TYP, default=NA)
    currency = models.CharField(
        max_length=120, null=True, blank=True, default='Ksh')
    inventory = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_image(self):
        if self.image is not None:
            return self.product.default_image
        else:
            return self.image

    def get_absolute_url(self):
        return self.product.get_absolute_url()


class ProductFeatured(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    text = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    FIVE = '5'
    FOUR = '4'
    THREE = '3'
    TWO = '2'
    ONE = '3'
    NUM = (
        (FIVE, '5'),
        (FOUR, '4'),
        (THREE, '3'),
        (TWO, '2'),
        (ONE, '1')
    )
    stars = models.CharField(max_length=10, choices=NUM, default=FIVE)
    caption = models.CharField(max_length=20, null=True, blank=True)
    review = models.TextField()
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


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
