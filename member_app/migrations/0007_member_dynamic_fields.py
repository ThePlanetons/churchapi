# Generated by Django 5.1.4 on 2025-01-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0006_rename_created_on_member_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dynamic_fields',
            field=models.JSONField(default=dict),
        ),
    ]
