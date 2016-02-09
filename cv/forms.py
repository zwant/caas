from django import forms

class CVForm(forms.Form):
    json_data = forms.CharField(label='CV As JSON', widget=forms.Textarea)
