def test_init(category1):
    assert category1.name == "Смартфоны"
    assert (category1.description == "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")


def test_category_product_property(category1):
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n')


def test_test_category_product_setter(category1, product1):
    assert len(category1.list_products) == 2
    category1.add_product(product1)
    assert len(category1.list_products) == 3
