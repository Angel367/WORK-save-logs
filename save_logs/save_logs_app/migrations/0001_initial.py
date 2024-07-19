# Generated by Django 5.0.7 on 2024-07-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_query', models.CharField(max_length=255)),
                ('search_date', models.DateTimeField(auto_now_add=True)),
                ('search_ip', models.GenericIPAddressField()),
                ('path', models.CharField(max_length=255)),
                ('status_code', models.IntegerField()),
            ],
        ),
    ]
