# Generated by Django 5.1.4 on 2025-03-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0011_alter_collection_transaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='date',
            field=models.DateField(),
        ),
    ]
