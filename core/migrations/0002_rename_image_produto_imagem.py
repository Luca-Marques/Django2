# Generated by Django 5.0.1 on 2024-01-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='imagem',
        ),
    ]
