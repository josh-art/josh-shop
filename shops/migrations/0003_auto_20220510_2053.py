# Generated by Django 2.2.14 on 2022-05-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_productfeatured_review_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeatured',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='title',
            new_name='name',
        ),
    ]