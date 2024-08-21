from django import forms

class UploadExcelForm(forms.Form):
    arquivo_excel = forms.FileField()