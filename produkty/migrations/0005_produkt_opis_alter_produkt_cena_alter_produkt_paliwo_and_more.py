# Generated by Django 4.0.1 on 2022-02-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0004_marka_remove_produkt_model_alter_produkt_marka'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='opis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='cena',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='paliwo',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Benzyna', 'Benzyna'), ('Hybryda', 'Hybryda'), ('Elektryczne', 'Elektryczne')], max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='marka',
            unique_together={('marka', 'model')},
        ),
    ]
