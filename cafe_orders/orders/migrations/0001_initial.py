# Generated by Django 4.2.18 on 2025-01-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название блюда')),
                ('price', models.FloatField(verbose_name='Цена блюда')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.SmallIntegerField(verbose_name='Номер стола')),
                ('total_price', models.FloatField(verbose_name='Общая стоимость заказа')),
                ('status', models.CharField(max_length=15, verbose_name='Статус заказа')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item', verbose_name='Список блюд')),
            ],
        ),
    ]
