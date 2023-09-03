from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseList(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    def get(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=expense_id)
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data)
        except Expense.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=expense_id)
            serializer = ExpenseSerializer(expense, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Expense.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Expense.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
