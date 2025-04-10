# Generated by Django 5.1.4 on 2025-01-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0005_member_config'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='member_config',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='member_config',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='member',
            name='created_by',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_by',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='member_config',
            name='created_by',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='member_config',
            name='updated_by',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
