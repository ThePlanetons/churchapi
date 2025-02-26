# Generated by Django 5.1.4 on 2025-02-26 11:11

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection_transaction',
            name='transaction_id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=20, unique=True),
        ),
    ]
