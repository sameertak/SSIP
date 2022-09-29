from django import forms

# Create your forms here.


class FeedbackForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email = forms.CharField(max_length = 264)
	password = forms.CharField(max_length = 50)