from django import forms

from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'other_author')



# dentist = forms.ModelChoiceField(queryset=Dentist.objects.all())
# office = forms.ModelChoiceField(queryset=Office.objects.all())