from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from players.models import AccountType, Player
from players.serializers import AccountTypeSerializer, PlayerSerializer


class PlayerListAPIView(ListAPIView):
    """Get players list.

    """
    permission_classes = (AllowAny,)
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()


class AccountTypeListAPIView(ListAPIView):
    """Get account types list.

    """
    permission_classes = (AllowAny,)
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer

    def get_queryset(self):
        return AccountType.objects.all()
