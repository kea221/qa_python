# qa_python
test_add_new_book_book_added(self) - проверяет, что книга добавлена в словарь books_genre.
test_add_new_book_length_name_not_from_0_to_41_book_not_added(self, length_name) - проверяет, что книги с длиной названия 0, 41, 42, и 116 символов не добавлены в словарь books_genre.
test_add_new_book_cant_add_the_book_twice(self) - проверяет, что одну книгу нельзя добавить дважды в словарь books_genre.
test_set_book_genre_if_book_in_books_genre_and_genre_in_genre_list_set_genre(self) - проверяет, что добавленной книге можно установить жанр, если книга есть в books_genre и её жанр входит в список genre.
test_set_book_genre_if_book_not_in_books_genre_genre_isnt_set(self): проверяет, что книге не добавленной в словарь books_genre нельзя установить жанр.
test_set_book_genre_if_genre_not_in_genre_list_genre_isnt_set(self): проверяет, что жанр не входящий в список genre не присваивается книге.
test_get_book_genre_genre_got(self) - проверяет, что жанр книги можно получить по имени книги
test_get_books_with_specific_genre_genre_got(self) - проверяет, что выводится список книг определённого жанра.
test_get_books_genre_books_genre_got(self) - проверяет, что выводится текущий словарь books_genre.
test_get_books_for_children_books_got(self) - проверяет, что возвращаются книги у которых жанр не входит в список genre_age_rating.
test_add_book_in_favorites_book_added(self) - проверяет, что книгу можно добавить в Избранное
test_delete_book_from_favorites_book_deleted(self) - проверяет, что книгу можно удалить из избранного.
test_get_list_of_favorites_books_list_got(self) - проверяет, что можно получить список избранных книг.