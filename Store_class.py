from Storage_abs_class import Storage
from exceptions import Over_capacity_exception


class Store(Storage):
    CAPACITY_MAY_BE = 100

    def __init__(self, name: str, dict={}):
        self._name = name
        self._items = dict

        if self._define_capacity() < 0:
            raise Over_capacity_exception
        else:
            self._capacity = self._define_capacity()

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, mark, quantity):
        if self._capacity >= quantity:
            current_qnt = self._items.get(mark, 0)
            self._items[mark] = current_qnt + quantity
            self._capacity -= quantity
        else:

            print(f"Требуется поместить на склад {quantity} единиц товара {mark}. На складе есть место только под " \
                  f"{self._capacity} единиц. Остаток, не размещенный на складе составляет "
                  f"{quantity - self._capacity} единиц.")
            self.add(mark, self._capacity)

    def remove(self, mark, quantity) -> dict:
        current_qnt = self._items.get(mark, None)

        if current_qnt is None:
            action = f"Товара {mark} вообще никогда не было на складе."
            return {"message": action, "are_we_cont": False}

        if current_qnt < quantity:
            self._items[mark] = 0
            self._capacity += current_qnt
            action = f"Товара {mark} на складе {self._name} всего {current_qnt} из запрашиваемых {quantity} ед.\nCо " \
                     f"склада" \
                     f" {self._name} " \
                     f"было изъято {current_qnt} единиц товара {mark}."
            return {"message": action, "are_we_cont": True, "transfered_count":current_qnt}
        else:
            self._items[mark] = current_qnt - quantity
            self._capacity += quantity
            action = f"Товар в полном обьеме ({quantity} шт.) есть на складе {self._name}.\nCо " \
                     f"склада {self._name} было изъято {quantity} единиц товара {mark}."
            return {"message": action, "are_we_cont": True,"transfered_count":quantity}

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(list(self._items.keys()))

    def _define_capacity(self):
        filled_cap = 0
        for i in self._items.values():
            filled_cap += i
        return self.CAPACITY_MAY_BE - filled_cap
