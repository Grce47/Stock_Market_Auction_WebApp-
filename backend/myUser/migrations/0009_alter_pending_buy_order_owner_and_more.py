# Generated by Django 4.1.2 on 2022-10-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myUser', '0008_alter_pending_buy_order_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_buy_order',
            name='owner',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='pending_sell_order',
            name='owner',
            field=models.CharField(max_length=32),
        ),
    ]