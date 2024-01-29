from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="7013",
        product_name="veniam",
        company_name="Cunha",
        manufacturing_date="2023-06-13",
        expiration_date="2052-10-23",
        serial_number="QS71 VBJ6 9851",
        storage_instructions="Facere quisquam exercitationem",
    )

    assert (
        str(product)
        == "The product 7013 - veniam with serial number QS71 VBJ6 9851 "
        "manufactured on 2023-06-13 by the company Cunha "
        "valid until 2052-10-23 must be stored according to the "
        "following instructions: Facere quisquam exercitationem."
    )
