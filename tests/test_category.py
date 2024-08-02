from src.category import Category


def test_init(category1):
    assert category1.name == "Смартфоны"
    assert (category1.description == "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")