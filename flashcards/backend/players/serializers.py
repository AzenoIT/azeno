from rest_framework import serializers

from players.models import Player, AccountType


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("uuid", "nick", "user", "account_type", "start_time", "expiration_time", "is_active", "created_at")


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ("id", "name", "duration", "cost")
