## Реализованные тесты

- `test_add_new_book_add_two_books` — проверка добавления двух разных книг.
- `test_add_new_book_genre_is_empty_by_default` — проверка, что у добавленной книги жанр по умолчанию пустой.
- `test_add_new_book_not_added_if_invalid_length` — проверка, что книга не добавляется, если имя пустое или длиннее 40 символов (параметризованный тест).
- `test_add_same_book_duplicate_not_added` — проверка, что одну и ту же книгу нельзя добавить дважды.
- `test_set_book_genre_success` — проверка успешной установки жанра книге.
- `test_set_book_genre_not_set_if_invalid_genre` — проверка, что жанр не устанавливается, если он отсутствует в списке допустимых.
- `test_get_books_with_specific_genre_return_correct_books` — проверка получения списка книг по указанному жанру.
- `test_get_books_for_children_not_return_books_with_age_rating` — проверка, что книги с возрастным рейтингом не попадают в список книг для детей.
- `test_add_book_in_favorites_success` — проверка добавления книги в избранное.
- `test_delete_book_from_favorites_success` — проверка удаления книги из избранного.