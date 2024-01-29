from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self._data = data if data is not None else []

    def add_data(self, data: List[Product]):
        self._data.extend(data)

    # propriedade apenas para leitura que retorna cópia da lista de produtos
    @property
    def data(self) -> List[Product]:
        return self._data.copy()
