# Generated by Django 4.0.1 on 2022-02-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0006_alter_marka_unique_together_modelauta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marka',
            name='marka',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
