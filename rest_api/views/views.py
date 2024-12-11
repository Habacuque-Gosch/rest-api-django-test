from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_api.models import Item
from rest_api.serializers import ItemSerializer
import json




@api_view(['GET'])
def get_items(request):

    if request.method == 'GET':

        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)

            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404)


@api_view(['POST'])
def add_item(request):

    if request.method == 'POST':

        try:
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)  
    
    return Response(status=status.HTTP_404_NOT_FOUND)
