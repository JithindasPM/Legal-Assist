# Generated by Django 5.0.2 on 2024-02-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_companydb_alter_legaldb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydb',
            name='ContactNo',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]
