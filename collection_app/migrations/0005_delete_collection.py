# Generated by Django 5.1.4 on 2025-02-26 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0004_alter_collection_transaction_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='collection',
        ),
    ]
