import os
from django.db import models
from django.conf import settings
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    description_long = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_promotional = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pro_img/%Y/%m', blank=True, null=True)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Varição'),
            ('S', 'Simples')
        )
    )

    def __str__(self):
        return self.name

    @staticmethod
    def resize_image(img, new_width=800):
        full_path_image = settings.MEDIA_ROOT / img.name
        image = Image.open(full_path_image)
        original_width, original_heigth = image.size

        if original_width > new_width:
            new_heigth = round((new_width * original_heigth) / original_width)
            new_image = image.resize((new_width, new_heigth), Image.LANCZOS)
            new_image.save(full_path_image, optimize=True, quality=50)

        image.close()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            self.resize_image(self.image)


class Variations(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_promotional = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    stock_min = models.IntegerField(default=5)

    def __str__(self):
        return self.name or self.product.name
