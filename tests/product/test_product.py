from inventory_report.product import Product


def test_create_product():
    id = "123"
    product_name = "Example Product"
    company_name = "Example Company"
    manufacturing_date = "2024-01-01"
    expiration_date = "2024-01-10"
    serial_number = "SN654123"
    storage_instructions = "Store in a cool, dry place."

    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )

    assert product.id == id
    assert product.product_name == product_name
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions
