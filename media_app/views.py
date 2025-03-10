from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import History, Bookmark, media_app
from .serializers import HistorySerializer, BookmarkSerializer
from django.http import HttpResponse, Http404
from rest_framework.generics import DestroyAPIView

# Home Page View
def home(request):
    return HttpResponse("Welcome to the Media Tracker!")

# 🔹 HISTORY: View & Add with Sorting
class HistoryList(APIView):
    def get(self, request):
        try:
            sort_param = request.query_params.get('sort', 'newest')  # Default: Newest first

            if sort_param == 'oldest':
                history = History.objects.all().order_by('timestamp')  # Oldest first
            elif sort_param == 'title':
                history = History.objects.all().order_by('media_app__title')  # Alphabetical order
            else:
                history = History.objects.all().order_by('-timestamp')  # Newest first (default)

            serializer = HistorySerializer(history, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            media_app_data = request.data.get('media_app')
            if not media_app_data:
                return Response({"error": "media_app field is required"}, status=status.HTTP_400_BAD_REQUEST)

            media_app_instance, created = media_app.objects.get_or_create(
                url=media_app_data['url'], 
                defaults={'title': media_app_data['title']}
            )

            history_item = History.objects.create(media_app=media_app_instance)

            return Response(HistorySerializer(history_item).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 🔹 HISTORY: Delete a Specific Entry
class HistoryDetailView(DestroyAPIView):
    queryset = History.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        try:
            history_entry = self.get_object()
            history_entry.delete()
            return Response({"message": "History entry deleted successfully"}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "History entry not found"}, status=status.HTTP_404_NOT_FOUND)

# 🔹 BOOKMARKS: View & Add with Sorting
class BookmarkList(APIView):
    def get(self, request):
        try:
            sort_param = request.query_params.get('sort', 'newest')  # Default: Newest first

            if sort_param == 'oldest':
                bookmarks = Bookmark.objects.all().order_by('id')  # Oldest first
            elif sort_param == 'title':
                bookmarks = Bookmark.objects.all().order_by('media_app__title')  # Alphabetical order
            else:
                bookmarks = Bookmark.objects.all().order_by('-id')  # Newest first (default)

            serializer = BookmarkSerializer(bookmarks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            media_app_data = request.data.get('media_app')
            if not media_app_data:
                return Response({"error": "media_app field is required"}, status=status.HTTP_400_BAD_REQUEST)

            media_app_instance, created = media_app.objects.get_or_create(
                url=media_app_data['url'], 
                defaults={'title': media_app_data['title']}
            )

            bookmark_item = Bookmark.objects.create(media_app=media_app_instance)

            return Response(BookmarkSerializer(bookmark_item).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 🔹 BOOKMARKS: Delete a Specific Entry
class BookmarkDetailView(DestroyAPIView):
    queryset = Bookmark.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        try:
            bookmark_entry = self.get_object()
            bookmark_entry.delete()
            return Response({"message": "Bookmark entry deleted successfully"}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Bookmark entry not found"}, status=status.HTTP_404_NOT_FOUND)

