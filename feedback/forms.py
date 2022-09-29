from django import forms

# Create your forms here.


class FeedbackForm(forms.Form):
	res1 = forms.CharField(max_length = 5)
	res2 = forms.CharField(max_length = 5)
	res3 = forms.CharField(widget = forms.Textarea, max_length = 200)