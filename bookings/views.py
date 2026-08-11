from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LSAProfile
from .serializers import BookingRequestSerializer, LSAProfileSerializer
from .services import verify_booking


class BookingRequestCreateView(APIView):

    def post(self, request):
        serializer = BookingRequestSerializer(data=request.data)

        if serializer.is_valid():
            booking = serializer.save()
            verify_booking(booking)

            return Response(
                BookingRequestSerializer(booking).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LSASearchView(APIView):

    def get(self, request):
        skill = request.query_params.get('skill')
        available = request.query_params.get('available')

        lsas = LSAProfile.objects.all()

        if skill:
            lsas = lsas.filter(skills__icontains=skill)

        if available == 'true':
            lsas = lsas.filter(is_active=True)

        serializer = LSAProfileSerializer(lsas, many=True)

        return Response(serializer.data)