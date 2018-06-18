from rest_framework import serializers

from pulse.models import Pulse


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     todos = serializers.HyperlinkedRelatedField(
#         many=True,
#         view_name='todos:todo-detail',
#         read_only=True
#     )
#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):
#         user = User(
#             username=validated_data.get('username', None)
#         )
#         user.set_password(validated_data.get('password', None))
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         for field in validated_data:
#             if field == 'password':
#                 instance.set_password(validated_data.get(field))
#             else:
#                 instance.__setattr__(field, validated_data.get(field))
#         instance.save()
#         return instance

#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username',
#                   'password', 'first_name', 'last_name',
#                   'email', 'todos'
#                   )
#         extra_kwargs = {
#             'url': {
#                 'view_name': 'users:user-detail',
#             }
#         }

class PulseSerializer(serializers.HyperlinkedModelSerializer):
    type=serializers.CharField(source='ctype')

    def create(self, validated_data):
        # valiated_data['ctype']=valiated_data['type']
        print(validated_data)
        pulse=Pulse(validated_data)
        pulse.save()
        return pulse

    def update(self, instance, validated_data):
        # valiated_data['ctype']=valiated_data['type']
        # del valiated_data['type']
        print(validated_data)
        for field in validated_data:
            instance.__setattr__(field, valiated_data.get(field))
            
    class Meta:
        model = Pulse
        fields = ('name', 'maximum_rabi_rate','polar_angle','type')

   