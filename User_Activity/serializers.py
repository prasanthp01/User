from rest_framework import serializers
from .models import UserAct

class UserActSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAct
        fields = ['id','real_name','list_act']

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'})
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = UserAct
        fields = ['username', 'real_name', 'id','email', 'password', 'confirm_password']

    def save(self):
        user = UserAct(email=self.validated_data['email'],
                    username=self.validated_data['username'],
                       real_name = self.validated_data['real_name'],
                       id = self.validated_data['id'])
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password not matched.'})
        user.set_password(password)
        user.save()
        return user
