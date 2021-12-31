from rest_framework import serializers

from moeda.models import Moeda


class MoedaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = (
            'initials',
            'name_coin',
            'data',
            'value'
        )


class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = (
            'initials',
            'name_coin',
            'data',
            'value'
        )
