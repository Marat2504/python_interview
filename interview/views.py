import uuid

from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from .models import Offer
from .serializers import OfferSerializer, AllOfferSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_offers(request):
    print(request.user)
    offers = list(request.user.offers.all())
    serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def offer_data(request, pk):
    try:
        offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
        return Response('Предложение не найдено', status=status.HTTP_404_NOT_FOUND)

    if offer.user != request.user:
        return Response('Нет доступа', status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = AllOfferSerializer(offer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = AllOfferSerializer(offer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_offer(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response('Нет доступа', status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'POST':
        new_uuid = str(uuid.uuid4())
        request.data['id'] = new_uuid
        serializer = AllOfferSerializer(data=request.data)
        if serializer.is_valid():
            offer = serializer.save()
            offer.user = request.user
            offer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





        # print(request.data['id'])
        # print(request.data['link'])
        # print(request.data['title'])
        # print(request.data['description'])
        # print(request.data['salary'])
        # print(request.data['location'])
        # print(request.data['employment_type'])
        # print(request.data['employment_type_display'])
        # print(request.data['status'])
        # print(request.data['status_display'])