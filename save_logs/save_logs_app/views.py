from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SearchLog
from .serializers import SearchLogSerializer


@api_view(['POST'])
def create_search_log(request):
    if request.method == 'POST':
        serializer = SearchLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
