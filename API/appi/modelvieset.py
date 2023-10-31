from .models import *
from .serializer import *
from rest_framework import viewsets

class studentapi(viewsets.ModelViewSet):
  queryset=student.objects.all()
  serializer_class=studentserializer
