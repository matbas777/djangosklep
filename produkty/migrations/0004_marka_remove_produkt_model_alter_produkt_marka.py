# Generated by Django 4.0.1 on 2022-02-01 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0003_produkt_title_obraz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='produkt',
            name='model',
        ),
        migrations.AlterField(
            model_name='produkt',
            name='marka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkty.marka'),
        ),
    ]
