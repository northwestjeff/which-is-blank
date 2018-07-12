from django.shortcuts import render
from whichisblank.models import Question, User, Author



def home(request):
    users = User.objects.all()
    authors = Author.objects.all()
    return render(request, 'whichisblank/home.html', {"authors": authors})

