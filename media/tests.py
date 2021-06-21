import unittest
import json
from rest_framework import status
from django.urls import reverse
from media.models import Media
from media.serializers import MediaSerializer
from rest_framework.test import APIClient

# initialize the APIClient app
client = APIClient()


# Test Cases
class TestModel1Api(unittest.TestCase):
    # Test data
    def setUp(self):
        self.valid_data = {
            'name': 'Car', 'media_type': "jpeg"
        }
        self.invalid_data = {
            'name': '', 'media_type': "jpeg"
        }
        self.pk = '4'

    # GET all elements
    def test_get_all_media_items(self):
        # get API response
        response = client.get(reverse('get_media_list'))
        # get data from db
        item_list = Media.objects.all()
        serializer = MediaSerializer(item_list, many=True)
        # validate
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # POST valid data
    def test_add_valid_media_items(self):
        # get API response
        response = client.post(reverse('get_media_list'), data=json.dumps(self.valid_data),
                               content_type='application/json')
        # validate
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # POST invalid data
    def test_add_invalid_media_items(self):
        # get API response
        response = client.post(reverse('get_media_list'), data=json.dumps(self.invalid_data),
                               content_type='application/json')
        # validate
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # GET single media item
    def test_get_media_item(self):
        item_list = Media.objects.get(pk=self.pk)
        serializer = MediaSerializer(item_list)
        # get API response
        response = client.get(reverse('get_media_details', kwargs={'pk': self.pk}))
        # validate
        self.assertEqual(serializer.data, response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # PUT media item
    def test_update_media_item(self):
        # get API response
        response = client.put(
            reverse('get_media_details', kwargs={'pk': self.pk}),
            data=json.dumps(self.valid_data),
            content_type='application/json')
        # validate
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # DELETE media item
    def test_delete_media_item(self):
        # get API response
        response = client.delete(reverse('get_media_details', kwargs={'pk': self.pk}))
        # validate
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
