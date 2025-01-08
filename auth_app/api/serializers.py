from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Call the original validate method to get the tokens
        data = super().validate(attrs)

        # Format the response to include tokens under the 'token' key
        data['token'] = {
            'refresh': data.pop('refresh'),
            'access': data.pop('access'),
        }

        # Add custom user data to the response
        data.update({
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'is_active': self.user.is_active,
            'name': f"{self.user.first_name} {self.user.last_name}",
            'last_login': self.user.last_login,
        })

        return data