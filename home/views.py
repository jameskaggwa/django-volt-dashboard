from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'name': 'james'
    }
    # Page from the theme
    # return render(request, 'pages/tables/bootstrap-tables.html', context)
    return render(request, 'pages/index.html', context)
    # return render(request, 'pages/components/forms.html', context)
