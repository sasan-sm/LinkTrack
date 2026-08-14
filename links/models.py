import secrets
import string

from django.contrib.auth.models import User
from django.db import models


def generate_unique_slug():
    chars = string.ascii_letters + string.digits
    max_attempts = 10

    for i in range (max_attempts):
        code = ''.join(secrets.choice(chars) for _ in range(6))

        if not ShortLink.objects.filter(slug=code).exists():
            return code

    return Exception("نمی‌تونم slug یکتا تولید کنم!")


class ShortLink(models.Model):
    original_url = models.URLField()
    slug = models.CharField(max_length=50, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = generate_unique_slug()

        # اضافه کردن http:// اگه وجود نداشت
        if not self.original_url.startswith(('http://', 'https://')):
            self.original_url = 'http://' + self.original_url

        super().save(*args, **kwargs)

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