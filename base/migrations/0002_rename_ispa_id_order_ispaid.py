# Generated by Django 5.2.4 on 2025-07-22 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='isPa_id',
            new_name='isPaid',
        ),
    ]
