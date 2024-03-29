# Generated by Django 4.2.11 on 2024-03-29 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15)),
                ('slug', models.SlugField(max_length=15, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(max_length=100)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('submitted_date',),
            },
        ),
    ]
