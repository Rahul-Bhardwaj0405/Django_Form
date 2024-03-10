from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Your_name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Name length should be within limit"
            },
            "review_text": {
                "required": "It must not be empty"
            },
            "rating": {
                    "required": "It must not be empty"
            }
        }

