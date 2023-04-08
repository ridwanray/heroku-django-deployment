# Generated by Django 4.0.6 on 2023-04-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='extra_info',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]