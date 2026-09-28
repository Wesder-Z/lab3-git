"""Классы животных для демонстрации наследования."""


class Animal:
    """Базовый класс животного."""

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Кличка животного не должна быть пустой")
        self.name = name

    def speak(self) -> str:
        """Задаёт интерфейс для голоса животного."""
        raise NotImplementedError("Метод должен быть переопределён")


class Dog(Animal):
    """Собака с собственной реализацией голоса."""

    def speak(self) -> str:
        """Возвращает голос собаки."""
        return f"{self.name} говорит: Гав!"
