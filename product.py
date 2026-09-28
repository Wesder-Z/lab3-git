"""Класс товара с управляемой ценой."""


class Product:
    """Хранит название товара и проверяет цену через property."""

    def __init__(self, name: str, price: float) -> None:
        if not name.strip():
            raise ValueError("Название товара не должно быть пустым")

        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """Текущая цена товара."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = float(value)
