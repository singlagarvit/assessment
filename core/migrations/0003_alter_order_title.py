# Generated by Django 3.2.4 on 2021-06-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_order_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
