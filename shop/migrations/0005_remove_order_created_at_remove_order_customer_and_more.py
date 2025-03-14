# Generated by Django 5.1.7 on 2025-03-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_phone_number_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Default Address', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='Default City', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='Default Country', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(default='000000', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='Default State', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
