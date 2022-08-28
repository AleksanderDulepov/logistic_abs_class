from Request_class import Request
from exceptions import Wrong_input_exception, Not_int_exception

desc="Ожидаемый формат ввода: Доставить 1 холодильник из ozon_store в ali_tmall"

def input_cycle(stores_dict,shops_dict):
    while True:
        try:
            order_input = input("Введите действие для выполнения:\n")
            order = Request(stores_dict, shops_dict, order_input)
        except Wrong_input_exception:
            print("Команда не может быть исполнена, формат введенной команды не соответствует")
            print(desc)
            continue
        except Not_int_exception:
            print("Команда не может быть исполнена, формат количества не соответсвует")
            print(desc)
        if order.where_from is None:
            print(f"Указанного склада нет в списке поставщиков")
            continue
        if order.to is None:
            print(f"Указанного магазина нет в списке клиентов")
            continue
        break
    return order
