# attachments/urls.py

from django.urls import path
from .views import AttachmentList, AttachmentDetail


urlpatterns = [
    path('attachments/', AttachmentList.as_view(), name='attachment-list'),
    path('attachments/<int:attachment_id>/', AttachmentDetail.as_view(), name='attachment-detail'),
]
