# Generated by Django 2.1 on 2019-09-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190922_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='cofeeBean',
            new_name='coffeeBean',
        ),
    ]
