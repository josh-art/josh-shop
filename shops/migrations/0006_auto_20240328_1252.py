# Generated by Django 2.2.14 on 2024-03-28 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20240327_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.DeleteModel(
            name='ProductFeatured',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
