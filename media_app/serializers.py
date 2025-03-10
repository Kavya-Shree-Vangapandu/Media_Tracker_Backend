from rest_framework import serializers
from .models import History, Bookmark, media_app

class media_appSerializer(serializers.ModelSerializer):
    class Meta:
        model = media_app
        fields = ['id', 'title', 'url']

class HistorySerializer(serializers.ModelSerializer):
    media_app = media_appSerializer()

    class Meta:
        model = History
        fields = ['id', 'media_app', 'timestamp']

class BookmarkSerializer(serializers.ModelSerializer):
    media_app = media_appSerializer()

    class Meta:
        model = Bookmark
        fields = ['id', 'media_app']
