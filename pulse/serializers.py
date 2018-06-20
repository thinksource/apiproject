from rest_framework import serializers

from pulse.models import Pulse


class PulseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(source='ctype')

    def create(self, validated_data):
        # valiated_data['ctype']=valiated_data['type']
        return Pulse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # valiated_data['ctype']=valiated_data['type']
        # del valiated_data['type']
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))

    class Meta:
        model = Pulse
        fields = ('id', 'name', 'maximum_rabi_rate', 'polar_angle', 'type')
