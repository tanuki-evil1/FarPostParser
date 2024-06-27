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
