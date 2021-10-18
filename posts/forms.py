from django import forms

from posts.models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    creator = forms.ModelChoiceField(
        queryset=None,
        empty_label=None,
    )

    class Meta:
        model = Post
        fields = ['title', 'text']

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['creator'].queryset = User.objects.filter(id=user.id)
