# Generated by Django 5.1.4 on 2025-03-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity_app', '0002_alter_entity_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='address',
            field=models.CharField(default=1, max_length=510),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='city',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='country',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='primary_phone',
            field=models.CharField(default=4, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='secondary_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='state',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='zip_code',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]
