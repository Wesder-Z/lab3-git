"""Расширенный список целых чисел."""


class NumberList(list[int]):
    """Добавляет операции над числами к встроенному списку."""

    def average(self) -> float:
        """Вычисляет среднее арифметическое элементов.

        Raises:
            ValueError: Если список пуст.
        """
        if not self:
            raise ValueError("Нельзя вычислить среднее пустого списка")
        return sum(self) / len(self)

    def even_numbers(self) -> "NumberList":
        """Создаёт новый список только с чётными числами."""
        return NumberList(number for number in self if number % 2 == 0)

    def squared(self) -> "NumberList":
        """Создаёт новый список квадратов чисел."""
        return NumberList(number**2 for number in self)
