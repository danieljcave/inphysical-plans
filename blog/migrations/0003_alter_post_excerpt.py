# Generated by Django 3.2.23 on 2023-12-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]