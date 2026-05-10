import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_genre_is_empty_by_default(self):
        collector = BooksCollector()

        collector.add_new_book("Python Book")

        assert collector.get_book_genre("Python Book") == ""

    @pytest.mark.parametrize("name", ["", "P" * 41])
    def test_add_new_book_not_added_if_invalid_length(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_same_book_duplicate_not_added(self):
        collector = BooksCollector()

        collector.add_new_book("В тихой степи")
        collector.add_new_book("В тихой степи")

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Лунный камень")

        collector.set_book_genre("Лунный камень", "Детективы")

        assert collector.get_book_genre("Лунный камень") == "Детективы"

    def test_set_book_genre_not_set_if_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("О дивный новый мир")

        collector.set_book_genre("О дивный новый мир", "Антиутопия")

        assert collector.get_book_genre("О дивный новый мир") == ""

    def test_get_books_with_specific_genre_return_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Константин")
        collector.add_new_book("Интерстеллар")

        collector.set_book_genre("Константин", "Ужасы")
        collector.set_book_genre("Интерстеллар", "Фантастика")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Константин"]

    def test_get_books_for_children_not_return_books_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Константин")
        collector.add_new_book("Проставквашино")

        collector.set_book_genre("Константин", "Ужасы")
        collector.set_book_genre("Проставквашино", "Мультфильмы")

        assert collector.get_books_for_children() == ["Проставквашино"]

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Интерстеллар")

        collector.add_book_in_favorites("Интерстеллар")

        assert collector.get_list_of_favorites_books() == ["Интерстеллар"]

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Интерстеллар")
        collector.add_book_in_favorites("Интерстеллар")

        collector.delete_book_from_favorites("Интерстеллар")

        assert collector.get_list_of_favorites_books() == []