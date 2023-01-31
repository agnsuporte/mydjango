from django.db import models
from django.utils.text import slugify
from django.conf import settings
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Produto')
    description = models.TextField(max_length=255, verbose_name='Descrição')
    description_long = models.TextField(verbose_name='Descrição Longa')
    slug = models.SlugField(unique=True, blank=True,
                            null=True, verbose_name='Slug (Branco para Auto)')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Preço')
    price_promotional = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, verbose_name='Preço Promocional')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(
        upload_to='pro_img/%Y/%m', blank=True, null=True, verbose_name='Imagem')
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples')
        ),
        verbose_name='Tipo Produto'
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
        if not self.slug:
            slug = slugify(f'{self.category}-{self.name}')
            self.slug = slug

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
