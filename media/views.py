from datetime import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from media.models import Media
from media.serializers import MediaSerializer
from rest_framework.decorators import api_view


# GET all Media items
# POST a Media item
# DELETE all Media Item

@api_view(['GET', 'POST', 'DELETE'])
def media_list(request):
    # Retrieve all elements
    if request.method == 'GET':
        item_list = Media.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            item_list = Media.filter(title__icontains=title)
        media_serializer = MediaSerializer(item_list, many=True)
        return JsonResponse(media_serializer.data, safe=False)
    # Add element into Database
    elif request.method == 'POST':
        media_data = JSONParser().parse(request)
        media_serializer = MediaSerializer(data=media_data)
        if media_serializer.is_valid():
            media_serializer.save()
            return JsonResponse(media_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete all elements from Database
    elif request.method == 'DELETE':
        count = Media.objects.all().delete()
        return JsonResponse({'message': '{} Media items were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


# GET Media item by Id
# PUT Media item by Id
# DELETE Media Item by Id


@api_view(['GET', 'PUT', 'DELETE'])
def media_details(request, pk):
    media_by_id = Media.objects.get(pk=pk)
    try:
        # Find element by Id
        if request.method == 'GET':
            media_serializer = MediaSerializer(media_by_id)
            return JsonResponse(media_serializer.data)
        # Update element by Id
        elif request.method == 'PUT':
            media_data = JSONParser().parse(request)
            media_data['update_datetime'] = datetime.now()
            media_serializer = MediaSerializer(media_by_id, data=media_data)
            if media_serializer.is_valid():
                media_serializer.save()
                return JsonResponse(media_serializer.data, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Delete element by Id
        elif request.method == 'DELETE':
            media_by_id.delete()
            return JsonResponse({'message': 'Media item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except media_by_id.DoesNotExist:
        return JsonResponse({'message': 'The media item does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
