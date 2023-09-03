from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer


class MaintenanceRequestList(APIView):
    def get(self, request):
        maintenance_requests = MaintenanceRequest.objects.all()
        serializer = MaintenanceRequestSerializer(maintenance_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaintenanceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaintenanceRequestDetail(APIView):
    def get(self, request, maintenance_request_id):
        try:
            maintenance_request = MaintenanceRequest.objects.get(id=maintenance_request_id)
            serializer = MaintenanceRequestSerializer(maintenance_request)
            return Response(serializer.data)
        except MaintenanceRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, maintenance_request_id):
        try:
            maintenance_request = MaintenanceRequest.objects.get(id=maintenance_request_id)
            serializer = MaintenanceRequestSerializer(maintenance_request, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MaintenanceRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, maintenance_request_id):
        try:
            maintenance_request = MaintenanceRequest.objects.get(id=maintenance_request_id)
            maintenance_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MaintenanceRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
