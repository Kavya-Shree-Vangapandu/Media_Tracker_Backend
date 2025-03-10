from django.db import models 

class media_app(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # URL must be unique

    def __str__(self):
        return self.title

class History(models.Model):
    media_app = models.ForeignKey(media_app, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History of {self.media_app.title}"

class Bookmark(models.Model):
    media_app = models.ForeignKey(media_app, on_delete=models.CASCADE)  

    def __str__(self):
        return f"Bookmark of {self.media_app.title}"

