# Generated by Django 5.0.2 on 2024-02-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LawyerDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(blank=True, max_length=25, null=True)),
                ('Qualification', models.TextField(blank=True, max_length=25, null=True)),
                ('EmailID', models.EmailField(blank=True, max_length=25, null=True)),
                ('Specialization', models.TextField(blank=True, max_length=25, null=True)),
                ('Username', models.TextField(blank=True, max_length=25, null=True)),
                ('Password', models.TextField(blank=True, max_length=25, null=True)),
                ('Appointment_time', models.TimeField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Lawyer_images')),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
