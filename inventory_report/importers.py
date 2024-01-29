from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file_json:
            data = json.load(file_json)
            products = []
            for elem in data:
                products.append(Product(
                    elem["id"],
                    elem["product_name"],
                    elem["company_name"],
                    elem["manufacturing_date"],
                    elem["expiration_date"],
                    elem["serial_number"],
                    elem["storage_instructions"],
                ))
        return products
            


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
