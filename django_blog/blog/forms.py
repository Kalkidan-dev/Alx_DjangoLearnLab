from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Clear existing tags
            instance.tags.clear()
            # Add new tags using django-taggit
            tag_names = [t.strip() for t in self.cleaned_data['tags'].split(',') if t.strip()]
            for name in tag_names:
                instance.tags.add(name)  # Add tags directly as strings
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
