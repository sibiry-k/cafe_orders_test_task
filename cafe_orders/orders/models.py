from django.db import models


class Item(models.Model):
    title = models.CharField(("Название блюда"), max_length=50)
    price = models.FloatField(("Цена блюда"))


class Order(models.Model):
    table_number = models.SmallIntegerField(("Номер стола"))
    items = models.ForeignKey(
        Item,
        verbose_name=("Список блюд"),
        on_delete=models.CASCADE
    )
    total_price = models.FloatField(("Общая стоимость заказа"))
    status = models.CharField(("Статус заказа"), max_length=15)
