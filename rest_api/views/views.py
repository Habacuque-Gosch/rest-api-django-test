from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_api.models import Item
from rest_api.serializers import ItemSerializer
import json




@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)

            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404)

@api_view(['GET'])
def get_by_name(request, name):

    try:
        user = Item.objects.get(name=name)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = ItemSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET','POST', 'PUT', 'DELETE'])
def user_manager(request):
    
    if request.method == 'GET':

        try:
            if request.GET['name']:

                name = request.GET['name']

                try:
                    user = Item.objects.get(name=name)
                except:
                    print('user not found')
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = ItemSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':

        new_user = request.data

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
    
        return Response(status=status.HTTP_404_NOT_FOUND)  
