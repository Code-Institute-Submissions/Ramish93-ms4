# Generated by Django 4.0.2 on 2022-03-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_attachment_as_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='subject',
            field=models.CharField(max_length=300),
        ),
    ]
