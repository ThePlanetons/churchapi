# Generated by Django 5.1.4 on 2025-03-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0013_collection_transaction_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection_transaction',
            name='transaction_id',
            field=models.CharField(editable=False, max_length=50, unique=True),
        ),
    ]
