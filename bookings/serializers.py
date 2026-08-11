from rest_framework import serializers

from .models import BookingRequest, LSAProfile


class BookingRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingRequest
        fields = [
            'id',
            'parent',
            'lsa',
            'start_time',
            'end_time',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'status', 'created_at']

    def validate(self, data):
        start_time = data['start_time']
        end_time = data['end_time']
        lsa = data['lsa']

        if start_time >= end_time:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        overlapping_booking = BookingRequest.objects.filter(
            lsa=lsa,
            start_time__lt=end_time,
            end_time__gt=start_time,
            status__in=['PENDING', 'CONFIRMED']
        ).exists()

        if overlapping_booking:
            raise serializers.ValidationError(
                "LSA is already booked during this time."
            )

        return data


class LSAProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = LSAProfile
        fields = [
            'id',
            'name',
            'email',
            'skills',
            'is_active',
            'created_at',
        ]