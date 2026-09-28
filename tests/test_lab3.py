"""Модульные тесты классов лабораторной работы №3."""

import unittest

from animals import Animal, Dog
from book import Book
from number_list import NumberList
from product import Product
from vector import Vector


class BookTests(unittest.TestCase):
    """Проверки класса книги."""

    def test_stores_book_information(self) -> None:
        book = Book("Капитанская дочка", "Александр Пушкин")

        self.assertEqual(book.title, "Капитанская дочка")
        self.assertEqual(book.author, "Александр Пушкин")
        self.assertIn("Капитанская дочка", str(book))

    def test_rejects_empty_title_and_author(self) -> None:
        with self.assertRaises(ValueError):
            Book("   ", "Александр Пушкин")
        with self.assertRaises(ValueError):
            Book("Капитанская дочка", "")


class AnimalTests(unittest.TestCase):
    """Проверки наследования классов животных."""

    def test_dog_inherits_from_animal(self) -> None:
        dog = Dog("Шарик")

        self.assertIsInstance(dog, Animal)
        self.assertEqual(dog.speak(), "Шарик говорит: Гав!")

    def test_base_method_requires_overriding(self) -> None:
        with self.assertRaises(NotImplementedError):
            Animal("Животное").speak()


class VectorTests(unittest.TestCase):
    """Проверки перегрузки оператора сложения."""

    def test_adds_vector_coordinates(self) -> None:
        result = Vector(2, 3) + Vector(4, -1)

        self.assertEqual(result.x, 6)
        self.assertEqual(result.y, 2)

    def test_rejects_addition_with_another_type(self) -> None:
        with self.assertRaises(TypeError):
            Vector(1, 2) + 5


class NumberListTests(unittest.TestCase):
    """Проверки подкласса встроенного списка."""

    def test_is_a_list(self) -> None:
        numbers = NumberList([1, 2, 3])

        self.assertIsInstance(numbers, list)

    def test_calculates_average(self) -> None:
        self.assertEqual(NumberList([2, 4, 6]).average(), 4)

    def test_filters_even_numbers(self) -> None:
        numbers = NumberList([1, 2, 3, 4, 5, 6])

        self.assertEqual(numbers.even_numbers(), [2, 4, 6])
        self.assertIsInstance(numbers.even_numbers(), NumberList)

    def test_builds_list_of_squares(self) -> None:
        self.assertEqual(NumberList([1, 2, 3]).squared(), [1, 4, 9])

    def test_rejects_average_of_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            NumberList().average()


class ProductTests(unittest.TestCase):
    """Проверки свойства цены товара."""

    def test_reads_and_updates_price(self) -> None:
        product = Product("Мышь", 1200)

        self.assertEqual(product.price, 1200.0)
        product.price = 999.5
        self.assertEqual(product.price, 999.5)

    def test_rejects_negative_price(self) -> None:
        with self.assertRaises(ValueError):
            Product("Мышь", -1)

    def test_rejects_non_numeric_price(self) -> None:
        product = Product("Мышь", 1200)

        with self.assertRaises(TypeError):
            product.price = "бесплатно"


if __name__ == "__main__":
    unittest.main()
