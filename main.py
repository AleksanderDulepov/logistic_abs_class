from Shop_class import Shop
from Store_class import Store
from utils import input_cycle

example = "Доставить 1 холодильник из ozon_store в ali_tmall"

# склады
dict_ozon_store = {"книга": 50, "велосипед": 10, "холодильник": 5}
dict_wild_store = {"матрас": 25, "утюг": 10, "тарелка": 25}

ozon_store = Store("ozon_store", dict_ozon_store)
wild_store = Store("wild_store", dict_wild_store)

stores_dict = [ozon_store, wild_store]

# магазины
dict_yandex_market = {"книга": 5, "велосипед": 3, "холодильник": 5}
dict_ali_tmall = {"матрас": 10, "утюг": 1, "холодильник": 1}

yandex_market = Shop("yandex_market", dict_yandex_market)
ali_tmall = Shop("ali_tmall", dict_ali_tmall)

shops_dict = [yandex_market, ali_tmall]

# диалог
order = input_cycle(stores_dict, shops_dict)
print(f"На момент получения команды в магазине {order.to.name} хранятся следующие товары:")
for product, amount in order.to.items.items():
    print(f"{product.capitalize()} - {amount} шт.")
print(f"Общая свободная емкость магазина {order.to.get_free_space()} ед.")

# проверка, а может ли склад принять такое количество товара
shop_work_with = order.to

free_space_for_item = shop_work_with.get_free_space_for_item(order.product, order.amount)
if free_space_for_item is None:
    print(f'В магазине нет места для размещения товара {order.product}')
    exit(0)
elif free_space_for_item != order.amount:
    print(
        f"В магазине есть место только под {free_space_for_item} единиц товара {order.product} из {order.amount}. Со склада будет "
        f"запрошена отгрузка только этого количество товара ({free_space_for_item} единиц).")
else:
    print(f"В магазине есть место под весь товар {order.product} в количестве {order.amount} ед. согласно запросу")

print(f"На момент запроса на перемещение на складе {order.where_from.name} хранятся следующие товары:")
for product, amount in order.where_from.items.items():
    print(f"{product.capitalize()} - {amount} шт.")

# проверка наличия на складе
remove_result = order.where_from.get_item_value(order.product, free_space_for_item)
if remove_result is None:
    print(f"Товара {order.product} вообще никогда не было на складе.")
    exit(0)
elif remove_result != free_space_for_item:
    print(
        f"Товара {order.product} на складе {order.where_from.name} всего {remove_result} из запрашиваемых {free_space_for_item} ед.")
    print(f"Со склада {order.where_from.name} было изъято {remove_result} единиц товара {order.product}.")
else:
    print(f"Товар в полном обьеме ({free_space_for_item} шт.) есть на складе {order.where_from.name}.")
    print(f"Со склада {order.where_from.name} было изъято {free_space_for_item} единиц товара {order.product}.")

order.where_from.remove(order.product, free_space_for_item)

# перемащение
print(f"Курьер везет {remove_result} {order.product} из {order.where_from.name} в {order.to.name}.")

# приходывание
order.to.add(order.product, remove_result)




print(f"Курьер доставил {remove_result} {order.product} в {order.to.name}.")
print(f"После перемещения в магазине {order.to.name} хранятся следующие товары:")
for product, amount in order.to.items.items():
    print(f"{product.capitalize()} - {amount} шт.")
print(f"Общая свободная емкость магазина {order.to.get_free_space()} ед.")
