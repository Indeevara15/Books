from django.shortcuts import render
from .serializers import BookSerializer
from .models import BooksModel
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
#the endpoints and their corresponding logic are defined using functions.

#read
@api_view(['GET'])
def Booklist(request):
    #if request.method == "GET":
        booksobj=BooksModel.objects.all()#queryset
        serializer=BookSerializer(booksobj,many=True)
        return Response(serializer.data)

#create
@api_view(['POST'])
def post_Book(request):
        booksobj=BooksModel.objects.all()#queryset
        serializer = BookSerializer(booksobj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

#update
@api_view(['POST'])
def update_Book(request,id):
    booksobj=BooksModel.objects.get(id=id)#queryset
    serializer=BookSerializer(instance=booksobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_Book(request,id):
    
    booksobj=BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("book is deleted")


