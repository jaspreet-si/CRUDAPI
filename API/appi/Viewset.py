from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status




class studentView(viewsets.ViewSet):

  def list(self,request):
    stu=student.objects.all()
    serializer=studentserializer(stu,many=True)
    
    return Response(serializer.data)
  
  def create(self,request):
    serializers=studentserializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self,request,pk=None):
    id=pk
    if id is not None:
      try:
        stu=student.objects.get(id=id)
        serializers=studentserializer(stu)
        return Response(serializers.data)
      except student.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
      
  def update(self,request,pk=None):
    id=pk
    stu=student.objects.get(id=id)
    serializers=studentserializer(stu,data=request.data)

    if serializers.is_valid():
      serializers.save()
      return Response({"msg":"Update successfully"})
    return Response(status=status.HTTP_304_NOT_MODIFIED)
  
  def partial_update(self,request,pk=None):
    id=pk
    stu=student.objects.get(id=id)
   
    serializers=studentserializer(stu,data=request.data,partial=True)
    if serializers.is_valid():
      serializers.save()
      return Response({"msg":"Update successfully"})
    return Response(status=status.HTTP_304_NOT_MODIFIED)
  
  def delete(Self,request,pk=None):
    id=pk
    stu=student.objects.get(id=id)
    stu.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)
      

      
