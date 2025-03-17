# Generated by Django 5.0.2 on 2024-03-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('EmailId', models.EmailField(blank=True, max_length=50, null=True)),
                ('Phn_No', models.IntegerField(blank=True, null=True)),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
