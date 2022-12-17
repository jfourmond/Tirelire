import logging

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from bank.exceptions import BrokenBankException, IntactBankException
from bank.models import Bank, BankContent
from bank.serializers import BankSerializer, BankContentSerializer, BankContentSaveSerializer


logger = logging.getLogger(__name__)


class BankView(ViewSet):

    def get_bank(self):
        try:
            bank = Bank.objects.latest("added")
        except Bank.DoesNotExist:
            logger.info("No piggy bank found, creating one.")
            bank, _ = Bank.objects.get_or_create()
        return bank

    def get_intact_bank(self):
        bank = self.get_bank()
        if bank.broken:
            raise BrokenBankException()
        return bank

    def list(self, request):
        bank = self.get_bank()
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    @action(detail=False, methods=["POST"], name="Break", url_path="break")
    def break_bank(self, request):
        """
        Casse la tirelire pour consulter et utiliser son contenu
        """
        bank = self.get_intact_bank()
        content = bank.content.all()

        serializer = BankContentSerializer(content, many=True)
        r = Response(serializer.data, status=status.HTTP_200_OK)
        # Casse de la tirelire
        bank.broken = True
        # Suppression du contenu
        content.delete()
        bank.save()
        return r

    @action(detail=False, methods=["POST"])
    def repare(self, _):
        """
        Crée une nouvelle tirelire
        """
        try:
            self.get_intact_bank()
            raise IntactBankException()
        except BrokenBankException:
            bank = Bank.objects.create()
            serializer = BankSerializer(bank)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"])
    def save(self, request):
        """
        Epargne de la monnaie, en y insérant des pièces et billets
        """
        bank = self.get_intact_bank()
        serializer = BankContentSaveSerializer(data=request.data)
        if serializer.is_valid():
            bank_content = BankContent(**serializer.validated_data)
            bank_content.bank = bank
            bank_content.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def shake(self, _):
        """
        Secoue la tirelire actuelle pour savoir combien il y a dedans
        """
        bank = self.get_intact_bank()
        content_value = sum([c.amount for c in bank.content.all()])
        return Response({"value": content_value}, status=status.HTTP_200_OK)
