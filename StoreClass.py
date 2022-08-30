from StorageAbcClass import Storage
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
        amount = self.get_free_space_for_item(quantity)
        current_qnt = self._items.get(mark, 0)
        self._items[mark] = current_qnt + amount
        self._capacity -= amount

    def remove(self, mark, quantity):
        current_qnt = self.get_item_value(mark, quantity)
        self._items[mark] = self._items.get(mark) - current_qnt
        self._capacity += current_qnt

    def get_item_value(self, mark, quantity):
        current_qnt = self._items.get(mark, None)
        if current_qnt is None:
            return None
        if current_qnt < quantity:
            return current_qnt
        else:
            return quantity

    def get_free_space_for_item(self, quantity):
        if self._capacity >= quantity:
            return quantity
        elif self._capacity > 0:
            return self._capacity
        else:
            return None

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
