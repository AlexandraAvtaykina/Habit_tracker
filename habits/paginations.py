from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """ Класс погинации с выводом 5 привычек на страницу """

    page_size = 5
