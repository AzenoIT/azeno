from rest_framework import pagination


class DecksPagination(pagination.LimitOffsetPagination):
    max_page_size = 100
