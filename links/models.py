from django.contrib.auth.models import User
from django.db import models


class ShortLink(models.Model):
    original_url = models.URLField()
    slug = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.slug} -> {self.original_url[:30]}"


class Click(models.Model):
    link = models.ForeignKey(ShortLink, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
    referrer = models.TextField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-clicked_at']

    def __str__(self):
        return f"Click on {self.link.slug} at {self.clicked_at}"