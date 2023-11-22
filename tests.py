from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        assert collector.get_books_genre() == {'Смерть на Ниле': ''}

    import pytest
    books = [
        '',
        'Советы юным леди по безупречной репутации',
        'Вязание без слёз. Базовые техники и схемы.',
        'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной царевне Лебеди'
    ]

    @pytest.mark.parametrize('length_name', books)
    def test_add_new_book_length_name_not_from_0_to_41_book_not_added(self, length_name):
        collector = BooksCollector()
        collector.add_new_book(length_name)
        assert length_name not in collector.get_books_genre()

    def test_add_new_book_cant_add_the_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.add_new_book('Смерть на Ниле')
        assert collector.get_books_genre() == {'Смерть на Ниле': ''}

    def test_set_book_genre_if_book_in_books_genre_and_genre_in_genre_list_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        assert collector.get_book_genre('Смерть на Ниле') == 'Детективы'

    def test_set_book_genre_if_book_not_in_books_genre_genre_isnt_set(self):
        collector = BooksCollector()
        collector.set_book_genre('Волшебник Земноморья', 'Фантастика')
        assert collector.get_book_genre('Волшебник Земноморья') == None

    def test_set_book_genre_if_genre_not_in_genre_list_genre_isnt_set(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert collector.get_book_genre('Война и мир') == ''

    def test_get_book_genre_genre_got(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        assert collector.get_book_genre('Смерть на Ниле') == 'Детективы'

    def test_get_books_with_specific_genre_genre_got(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre_books_genre_got(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Смерть на Ниле': 'Детективы', 'Оно': 'Ужасы'}

    def test_get_books_for_children_books_got(self):
        collector = BooksCollector()
        collector.add_new_book('Дневник фокса Микки')
        collector.set_book_genre('Дневник фокса Микки', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Дневник фокса Микки']

    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Турецкий гамбит')
        collector.add_book_in_favorites('Турецкий гамбит')
        assert 'Турецкий гамбит' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Турецкий гамбит')
        collector.add_book_in_favorites('Турецкий гамбит')
        collector.delete_book_from_favorites('Турецкий гамбит')
        assert 'Турецкий гамбит' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_list_got(self):
        collector = BooksCollector()
        collector.add_new_book('Турецкий гамбит')
        collector.add_book_in_favorites('Турецкий гамбит')
        assert collector.get_list_of_favorites_books() == ['Турецкий гамбит']
