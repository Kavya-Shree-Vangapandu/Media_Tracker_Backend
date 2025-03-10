from django.urls import path
from .views import HistoryList, HistoryDetailView, BookmarkList, BookmarkDetailView

urlpatterns = [
    # History Routes
    path('history/', HistoryList.as_view(), name='history_list'),  # View & Add History
    path('history/<int:id>/', HistoryDetailView.as_view(), name='history_detail'),  # Delete History Entry

    # Bookmark Routes
    path('bookmarks/', BookmarkList.as_view(), name='bookmark_list'),  # View & Add Bookmarks
    path('bookmarks/<int:id>/', BookmarkDetailView.as_view(), name='bookmark_detail'),  # Delete Bookmark Entry
]
