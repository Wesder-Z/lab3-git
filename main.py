"""Демонстрация заданий лабораторной работы №3."""

from animals import Dog
from book import Book
from number_list import NumberList
from product import Product
from vector import Vector


def main() -> None:
    """Последовательно показывает работу созданных классов."""
    book = Book("Мастер и Маргарита", "Михаил Булгаков")
    print(f"Книга: {book}")

    dog = Dog("Шарик")
    print(f"Наследование: {dog.speak()}")

    first_vector = Vector(2, 3)
    second_vector = Vector(4, 1)
    print(f"Сложение векторов: {first_vector + second_vector}")

    numbers = NumberList([1, 2, 3, 4, 5, 6])
    print(f"Расширенный список: {numbers}")
    print(f"Среднее: {numbers.average()}")
    print(f"Чётные числа: {numbers.even_numbers()}")
    print(f"Квадраты: {numbers.squared()}")

    product = Product("Клавиатура", 2500)
    product.price = 2300
    print(f"Товар: {product.name}, цена: {product.price:.2f}")


if __name__ == "__main__":
    main()
