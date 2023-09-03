# attachments/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentList(APIView):
    def get(self, request):
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentDetail(APIView):
    def get(self, request, attachment_id):
        try:
            attachment = Attachment.objects.get(id=attachment_id)
            serializer = AttachmentSerializer(attachment)
            return Response(serializer.data)
        except Attachment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, attachment_id):
        try:
            attachment = Attachment.objects.get(id=attachment_id)
            attachment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Attachment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
