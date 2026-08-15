from django import forms
from .models import ShortLink

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'لینک بلند خود را وارد کنید',
                'required': True,
            })
        }
        labels = {
            'original_url': 'آدرس وب سایت',
        }
        help_texts = {
            'original_url': 'مثال: https://example.com/page',
        }
        error_messages = {
            'original_url': {
                'required': 'وارد کردن آدرس الزامی است',
                'invalid': 'لطفاً یک آدرس معتبر وارد کنید'
            }
        }