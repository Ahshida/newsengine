__author__ = 'Vignesh Prakasam'

from django import forms


class SearchForm(forms.Form):
    searchTerm = forms.CharField()