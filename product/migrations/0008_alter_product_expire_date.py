# Generated by Django 3.2.10 on 2021-12-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(max_length=155),
        ),
    ]
