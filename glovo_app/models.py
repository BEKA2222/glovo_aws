from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxLengthValidator, MinLengthValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG')
    ROLE_CHOICES = (
        ('client', 'client'),
        ('courier', 'courier' ),
        ('owner', 'owner')
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='client')
    user_image = models.ImageField(upload_to='user_image')


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    store_image = models.ImageField(upload_to='store-images')
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name_contact = models.CharField(max_length=32)
    phone_number = PhoneNumberField(region='KG')


class Address(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)