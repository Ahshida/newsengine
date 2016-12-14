__author__ = 'Ash'

from django import forms


class SearchForm(forms.Form):
    searchTerm = forms.CharField()
