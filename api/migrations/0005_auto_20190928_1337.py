# Generated by Django 2.1 on 2019-09-28 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190928_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='coffeeBean',
            new_name='cofeeBean',
        ),
    ]
