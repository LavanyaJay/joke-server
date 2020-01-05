from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import JokeSerializer      # add this
from .models import Joke                     # add this


class JokeView(viewsets.ModelViewSet):       # add this
    serializer_class = JokeSerializer          # add this
    queryset = Joke.objects.all()
