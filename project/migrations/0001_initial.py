# Generated by Django 4.1 on 2022-09-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
