from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import AnnouncementSerializer

from api.models import Announcement


class IndexAPIView(APIView):

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)


class AnnouncementAPIView(APIView):

    def get(self, request, *args, **kwargs):
        announcement = get_object_or_404(Announcement, id=kwargs['id'])
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        announcement = get_object_or_404(Announcement, id=kwargs['id'])
        serializer = AnnouncementSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        announcement = get_object_or_404(Announcement, id=kwargs['id'])
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnnouncementCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
