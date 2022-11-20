from django.forms import ModelForm
from django import forms
from .models import books, rewards, requests

class BookForm(ModelForm):
    description = forms.CharField( widget=forms.Textarea )
    wordbyauthor = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = books

        exclude = ['bookuser', 'addtocart', 'bookrewards']
         


class RewardForm(ModelForm):
    class Meta:
        model = rewards
        fields = ['rewardname', 'rewardimage']



    #     requestedbooks = models.ManyToManyField('books',  default= None)
    # requesteduser = models.ForeignKey('User', on_delete=models.CASCADE,default=None)
    # requestaddress = models.CharField(max_length=500, default=None)
    # requestphone = mo