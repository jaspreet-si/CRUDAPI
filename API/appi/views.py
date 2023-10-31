from django.shortcuts import render
from .models import student
from .serializer import studentserializer  # Correct the import and capitalize the serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView





@api_view(['GET','POST'])


def api(request):
    if request.method == 'GET':
        info = student.objects.all()
        serializer = studentserializer(info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':  # Correct the conditional
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return a 201 status code for a successful POST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def make_changes_api(request,id):
    try:
        info = student.objects.get(id=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentserializer(info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = studentserializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PATCH':
        serializer=studentserializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)

    elif request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def abc(request, pk=None):
    
    if request.method == 'GET':
        info = student.objects.all()
        serializer = studentserializer(info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            student_instance = student.objects.get(id=pk)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = studentserializer(student_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        try:
            student_instance = student.objects.get(id=pk)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = studentserializer(student_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            student_instance = student.objects.get(id=pk)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#class based API

class StudentApi(APIView):
    def get(self,request,id=None,format=None):
        id=id
        if id is not None:
            try: #try this if  there id mention in url 
                stu=student.objects.get(id=id)
                serializer=studentserializer(stu)
                return Response(serializer.data)
            except student.DoesNotExist: # if student is not exist in the model then try this
                return Response({"msg":f"{id} does not exist "},status=status.HTTP_404_NOT_FOUND)
        
        stu=student.objects.all()
        serializer=studentserializer(stu,many=True)

        return Response(serializer.data)
    
    def post(self,request,id,format=None):
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Post successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        

        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data updated"})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
    def patch(self,request,id,format=None):
        

        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=request.data,partial=True)
       
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"updates succesfully"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        
        stu=student.objects.get(id=id)
        
        
        stu.delete()
        return Response({"msg":"delete successfully"})
        





    



    


