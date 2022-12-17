from rest_framework import serializers
from bank.models import Bank, BankContent


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"
        read_only_fields = ["id", "broken", "added", "updated"]


class BankContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankContent
        fields = ["id", "type", "amount", "added"]
        read_only_fields = ["id", "added"]


class BankContentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankContent
        fields = ["type", "amount"]
