# Let's see, so far we have added our app to installed apps on settings.py,
# Then we have made our views here, after that we made urls.py on our app and added the urlpatterns with the paths and all
# And then we went to the big urls.py on the project directory and included that same urls.py of the app

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from datetime import *

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "killings/cum.html", {
        "cum": now.month == 8 and now.day == 3
    })

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}! <3")

# def greet(request, name):
#     return render(request, "killings/greet.html", {"name": name})

tusks = []
class Tusk(forms.Form):
    tusk = forms.CharField(label="Tooth")
    heaftiness = forms.IntegerField(label="How heavy is your toothache?", min_value=1, max_value=3)

def tusk(request):
    return render(request, "killings/tusk.html", {
        "tusks": tusks
    })

def confessionary(request):
    if request.method == "POST":
        form = Tusk(request.POST)
        if form.is_valid():
            tsk = form.cleaned_data["tsk"]
            tusks.append(tsk)
        else:
            return render(request, "killings/confessionary.html", {
                "form": form
            })
    return render(request, "killings/confessionary.html", {
        "form": Tusk()
    })