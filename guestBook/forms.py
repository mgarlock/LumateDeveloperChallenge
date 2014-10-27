#forms.py
from django import forms
from guestBook.models import GuestLog

class GuestLogForm(forms.ModelForm):
  class Meta:
    model = GuestLog
    fields = ('f_name', 'l_name', 'favorite_dino')
