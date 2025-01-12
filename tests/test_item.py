import pytest
from src.item import Item
from src.exception_class import InstantiateCSVError


@pytest.fixture
def laptop():
    return Item("Ноутбук", 20000, 5)

def test_item_init(laptop):
    """Test of initialization of the class Item"""
    assert laptop.name == "Ноутбук"
    assert laptop.price == 20000
    assert laptop.quantity == 5
    assert len(Item.all) == 1

def test_item_calculate_total_price(laptop):
    """Test of the method calculate_total_price"""
    assert laptop.calculate_total_price() == 100000

def test_item_apply_discount(laptop):
    """"Test of the method apply_discount"""
    laptop.apply_discount()
    assert laptop.price == 20000

def test_item_name(laptop):
    """Test of the method name"""
    assert laptop.name == 'Ноутбук'

def test_item_new_name():
    """Test of the change of the name"""
    item = Item("Ноут", 20000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
def test_item_name_more_than_ten(laptop):
    """Test of the item name with length greater than 10 signs"""
    with pytest.raises(Exception, match="Длина наименования товара превышает 10 символов"):
        laptop.name = "01234567890"

def test_item_name_less_than_ten(laptop):
    """Test of the item name with length less than 10 signs"""
    Item.name = 'Смартфон'
    assert Item.name == 'Смартфон'
    Item.name = 'Ноутбук'
    assert Item.name == 'Ноутбук'

def test_item_instantiate_from_csv_good():
    """Test  of the method instantiate_from_csv"""
    Item.all.clear()
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_item_instantiate_from_csv_no_file():
    """Test  of the method instantiate_from_csv with no file"""
    Item.all.clear()
    Item.CSV_FILE = "../src/items2.csv"
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv()

def test_item_instantiate_from_csv_broken_file():
    """Test  of the method instantiate_from_csv with a broken csv file"""
    Item.all.clear()
    Item.CSV_FILE = "../tests/items_test.csv"
    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv()


def test_item_instantiate_from_csv_broken_file_2():
    """Test  of the method instantiate_from_csv with a broken csv file"""
    Item.all.clear()
    Item.CSV_FILE = "../tests/items_test_2.csv"
    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv()

def test_item_string_to_number():
    """Test  of the method string_to_number"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(laptop):
    """Test if the __repr__ method"""
    assert repr(laptop) == "Item('Ноутбук', 20000, 5)"

def test_str(laptop):
    """Test if the __str__ method"""
    assert str(laptop) == 'Ноутбук'
