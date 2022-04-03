from django import forms

FLATS= [
    (0, "1 ROOM"),
    (1, "2 ROOM"),
    (2, "3 ROOM"),
    (3, "4 ROOM"),
    (4, "5 ROOM"),
    (5, "MULTI GENERATION"),
    (7, "EXECUTIVE")
    ]

class DetailForm(forms.Form):

    year = forms.CharField(label="Year", max_length=4, min_length=4)
    month = forms.CharField(label="Month", max_length=2, min_length=2)

    area_sqm = forms.IntegerField(label="Area")
    f_type = forms.CharField(label="Apartment Type", widget=forms.Select(choices=FLATS))


    



