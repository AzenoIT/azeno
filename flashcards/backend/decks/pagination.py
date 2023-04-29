from rest_framework import pagination


class DecksPagination(pagination.LimitOffsetPagination):
    max_limit = 100
