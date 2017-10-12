from django import forms

class AddMusicForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Music Name'}),
    required=True, min_length=6, max_length=75)
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Youtube Video Code'}),
    required=True, min_length=2, max_length=75)

class GeneratePlaylistForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Playlist Name'}),
    required=True, min_length=6, max_length=75)
    description =  forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Description'}),
    required=True, min_length=2, max_length=75)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'validate', 'placeholder':'E-mail'}), required=True)
