from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer


class PropertyList(APIView):
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetail(APIView):
    def get(self, request, property_id):
        try:
            property = Property.objects.get(id=property_id)
            serializer = PropertySerializer(property)
            return Response(serializer.data)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, property_id):
        try:
            property = Property.objects.get(id=property_id)
            serializer = PropertySerializer(property, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, property_id):
        try:
            property = Property.objects.get(id=property_id)
            property.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
