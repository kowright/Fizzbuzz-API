# Generated by Django 5.0.3 on 2024-03-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fizzbuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(primary_key=True, serialize=False)),
                ('useragent', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]