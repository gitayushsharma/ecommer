# Generated by Django 4.1 on 2023-06-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustId', models.CharField(max_length=255)),
                ('CName', models.CharField(max_length=255)),
                ('PhoneNum', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Adrs', models.CharField(max_length=255)),
            ],
        ),
    ]
