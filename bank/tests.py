from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bank.exceptions import BrokenBankException, IntactBankException
from bank.models import Bank, BankContent
from bank.serializers import BankSerializer, BankContentSerializer, BankContentSaveSerializer


class BankTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.bank_1 = Bank.objects.create()
        cls.bank_2 = Bank.objects.create()

        cls.bank_content_1 = BankContent.objects.create(bank=cls.bank_2, amount=10, type="bank_note")
        cls.bank_content_2 = BankContent.objects.create(bank=cls.bank_2, amount=5, type="bank_note")
        cls.bank_content_3 = BankContent.objects.create(bank=cls.bank_2, amount=2, type="coin")
        cls.bank_content_4 = BankContent.objects.create(bank=cls.bank_2, amount=2, type="coin")
        cls.bank_contents = [cls.bank_content_1, cls.bank_content_2, cls.bank_content_3, cls.bank_content_4]

    def test_break(self):
        url = reverse("bank-break-bank")
        # Test on Intact
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BankContentSerializer(BankTests.bank_contents, many=True)
        self.assertEqual(response.data, serializer.data)

        # Test on Broken
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.data["detail"], BrokenBankException.default_detail)

    def test_get(self):
        response = self.client.get(reverse("bank-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BankSerializer(BankTests.bank_2)
        self.assertEqual(response.data, serializer.data)

    def test_repare(self):
        url = reverse("bank-repare")

        # On intact piggy bank
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.data["detail"], IntactBankException.default_detail)

        # On broken piggy bank
        self.client.post(reverse("bank-break-bank"))
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_save(self):
        data = {"amount": 50, "type": "bank_note"}

        url = reverse("bank-save")

        # On intact Piggy Bank
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        serializer = BankContentSaveSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(response.data, serializer.data)

        # On broken piggy bank
        self.client.post(reverse("bank-break-bank"))
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.data["detail"], BrokenBankException.default_detail)

    def test_shake(self):
        url = reverse("bank-shake")
        expected_sum = sum([c.amount for c in BankTests.bank_contents])

        # On intact biggy bank
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BankSerializer(BankTests.bank_2)
        self.assertEqual(response.data, {"value": expected_sum})

        # On broken piggy bank
        self.client.post(reverse("bank-break-bank"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.data["detail"], BrokenBankException.default_detail)
