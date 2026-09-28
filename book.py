"""Класс книги."""


class Book:
    """Хранит название книги и имя автора."""

    def __init__(self, title: str, author: str) -> None:
        if not title.strip():
            raise ValueError("Название книги не должно быть пустым")
        if not author.strip():
            raise ValueError("Имя автора не должно быть пустым")

        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Формирует строку с информацией о книге."""
        return f'"{self.title}", автор: {self.author}'
