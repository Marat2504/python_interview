from rest_framework import serializers

from interview.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'title', 'salary', 'employment_type', 'link', 'status')


class AllOfferSerializer(serializers.ModelSerializer):
    employment_type_display = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = ('id', 'title', 'link', 'description', 'salary', 'location', 'employment_type',
                  'employment_type_display', 'publish_date', 'contact_info', 'comments', 'status', 'status_display')

    def get_employment_type_display(self, obj):
        return {obj.employment_type: obj.get_employment_type_display()}

    def get_status_display(self, obj):
        return {obj.status: obj.get_status_display()}