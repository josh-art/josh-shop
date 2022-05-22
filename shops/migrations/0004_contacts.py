# Generated by Django 2.2.14 on 2022-05-12 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20220510_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(max_length=300)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('submitted_date',),
            },
        ),
    ]
