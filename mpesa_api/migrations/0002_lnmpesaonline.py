# Generated by Django 3.2.8 on 2021-10-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LNmpesaOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
