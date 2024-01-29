from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="7013",
        product_name="veniam",
        company_name="Cunha",
        manufacturing_date="2023-06-13",
        expiration_date="2052-10-23",
        serial_number="QS71 VBJ6 9851 8Q7P E4D4 JNYC 3X25",
        storage_instructions="Facere quisquam etc..",
    )

    assert product.id == "7013"
    assert product.product_name == "veniam"
    assert product.company_name == "Cunha"
    assert product.manufacturing_date == "2023-06-13"
    assert product.expiration_date == "2052-10-23"
    assert product.serial_number == "QS71 VBJ6 9851 8Q7P E4D4 JNYC 3X25"
    assert product.storage_instructions == "Facere quisquam etc.."
