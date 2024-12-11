from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item


@api_view(['GET'])
def getData(request):

    person = {'name': 'Kitana', 'age': 19}

    # items = Item.objects.all()

    return Response(person)