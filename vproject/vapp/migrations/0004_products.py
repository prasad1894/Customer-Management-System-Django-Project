# Generated by Django 5.0.4 on 2024-05-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0003_rename_vendor_code_customer_vendor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
