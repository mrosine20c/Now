from accounts.models import  User
from rest_framework import generics,status,permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from accounts.permissions import IsStudentUser,IsInstructortUser
from .serializers import(UserSerializer,RegisterInstructorSerializer,
RegisterStudentSerializer) 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class InstructorRegisterView(generics.GenericAPIView):
    serializer_class=RegisterInstructorSerializer
    def post(self,request, *args, **Kwargs):
         serializer=self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         user=serializer.save()
         user_serializer = UserSerializer(user, context=self.get_serializer())
         return Response(
            {
            "user": user_serializer.data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
            }
         )



class StudentRegisterView(generics.GenericAPIView):
    serializer_class=RegisterStudentSerializer
    
    def post(self,request, *args, **Kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        user_serializer = UserSerializer(user, context={'request': request})
        return Response({
            "user": user_serializer.data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })
 

# ## logingin in
# class CustomAuthToken(ObtainAuthToken):
#     def get(self, request, *args, **kwargs):
#         # Return a login form for GET requests
#         return Response({'message': 'Please provide username and password.'})

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'is_student': user.is_student,
#             'is_instructor': user.is_instructor,
#         })

from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                return Response({'token': user.auth_token.key})
            else:
                return Response({'error': 'Account is disabled'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)





## logout user
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Delete the user's token
        request.auth.delete()
        return Response({'message': 'Logged out successfully.'})


## student Dashboard
class Studentonlyview(generics.RetrieveAPIView):
   permission_classes=[permissions.IsAuthenticated & IsStudentUser] 
   serializer_class=UserSerializer     
   def get_object(self):
      return self.request.user

## Instructor Dashboard
class Instructortonlyview(generics.RetrieveAPIView):
   permission_classes=[permissions.IsAuthenticated & IsInstructortUser] 
   serializer_class=UserSerializer     
   def get_object(self):
      return self.request.user 


from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm

class ChangePasswordView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        # Create a password change form with the request data
        form = PasswordChangeForm(user, request.data)
        if form.is_valid():
            form.save()
            # Return success response
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        else:
            # Return validation error response
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
#creating a course

        
        

        







