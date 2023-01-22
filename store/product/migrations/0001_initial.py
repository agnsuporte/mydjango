# Generated by Django 4.1.5 on 2023-01-21 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('description_long', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_promotional', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pro_img/%Y/%m')),
                ('stock', models.IntegerField()),
                ('stock_min', models.IntegerField()),
                ('product_type', models.CharField(choices=[('V', 'Varição'), ('S', 'Simples')], default='V', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]