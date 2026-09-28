"""Двумерный вектор с перегруженным оператором сложения."""


class Vector:
    """Представляет вектор на плоскости."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: object) -> "Vector":
        """Складывает два вектора покомпонентно."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        """Формирует строковое представление вектора."""
        return f"Vector(x={self.x}, y={self.y})"
