# Generated by Django 4.0.2 on 2022-02-23 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Available'), ('Coming-Soon', 'Coming-Soon'), ('Out-of-Stock', 'Out-of-Stock')], max_length=30, null=True)),
                ('image', models.ImageField(default='', upload_to='gallery_item/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
