# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def smart_home(request):
    responce_data = {'message': 'Hellow'}
    return Response(responce_data)
