# Generated by Django 5.0.2 on 2024-03-06 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_lawyerdb_mob_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdb',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userdb',
            old_name='Username',
            new_name='username',
        ),
    ]
