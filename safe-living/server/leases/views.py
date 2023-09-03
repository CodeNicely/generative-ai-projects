from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lease
from .serializers import LeaseSerializer


class LeaseList(APIView):
    def get(self, request):
        leases = Lease.objects.all()
        serializer = LeaseSerializer(leases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeaseDetail(APIView):
    def get(self, request, lease_id):
        try:
            lease = Lease.objects.get(id=lease_id)
            serializer = LeaseSerializer(lease)
            return Response(serializer.data)
        except Lease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, lease_id):
        try:
            lease = Lease.objects.get(id=lease_id)
            serializer = LeaseSerializer(lease, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Lease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, lease_id):
        try:
            lease = Lease.objects.get(id=lease_id)
            lease.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Lease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
