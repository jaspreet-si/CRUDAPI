from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


 
# method 1
class studentCP(GenericAPIView,ListModelMixin,CreateModelMixin):
  queryset=student.objects.all()
  serializer_class=studentserializer

  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)
  
  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)
  
class RUDAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
  queryset=student.objects.all()
  serializer_class=studentserializer

  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

# method 2
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class studentgeneric(ListCreateAPIView):
  queryset=student.objects.all()
  serializer_class=studentserializer

class RUD(RetrieveUpdateDestroyAPIView):
  queryset=student.objects.all()
  serializer_class=studentserializer
