from Shop_class import Shop
from Store_class import Store

class Request():

    def __init__(self, stores: list[Store], shops: list[Shop], request: str):
        self._stores=stores
        self._shops=shops
        self._request=request
        self._create_output()

    def _create_output(self):
        if self._check_valid_input():
            self._amount = self._check_valid_amount(self._request.split(" ")[1])
            self._product = self._request.split(" ")[2]
            self._where_from = self._request.split(" ")[4]
            self._to = self._request.split(" ")[6]
        else:
            raise Wrong_input_exception

    def _check_valid_amount(self,value):
        if value.isdigit():
            return int(value)
        raise Not_int_exception


    def _check_valid_input(self)->bool:
        if len(self._request.split(" ")) == 7:
            return True
        return False

    def _find_storage(self):
        for i in self._stores:
            if self._where_from==i.name:
                return i
        return None

    def _find_shop(self):
        for i in self._shops:
            if self._to==i.name:
                return i
        return None

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    @property
    def where_from(self):
        return self._find_storage()

    @property
    def to(self):
        return self._find_shop()
