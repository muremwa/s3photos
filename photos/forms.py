from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from .models import Post


class PostForm(forms.Form):
    file = forms.ImageField(help_text='Choose an image')
    caption = forms.CharField(max_length=200, widget=forms.Textarea, help_text='Tell others what the image is about')
    your_name = forms.CharField(max_length=400, help_text='Enter a name you would like to be known as')

    def clean_your_name(self):
        data = self.cleaned_data['your_name']
        if len(data) < 2:
            raise ValidationError(_("A valid name needs be longer than '{}'".format(str(data))))
        return data

    def clean_caption(self):
        data = self.cleaned_data['caption']
        if not data:
            raise ValidationError(_('We think you image needs a caption to say what it\'s about.'))
        return data

    def save(self):
        data = self.cleaned_data
        new_post = Post(
            uploaded_by=data['your_name'],
            image_file=data['file'],
            caption=data['caption']
        )
        new_post.save()
