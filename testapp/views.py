from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi 

# Create your views here.
class TestCreate(CreateAPIView):
    serializer_class = TestSerializer

    @swagger_auto_schema(
        tags=["TestCreateView"],
        operation_description="Your custom operation description",
        responses={201: "Created"},
        request_body=TestSerializer,
    )
    def post(self, request):
        return super().post(self, request)
    
    

class GetTest(APIView):
    serializer_class = TestSerializer
    test_id = openapi.Parameter('test_id', openapi.IN_PATH, description='test_id path', required=True, type=openapi.TYPE_NUMBER)
    @swagger_auto_schema(tags=['테스트 Get API'], manual_parameters=[test_id], responses={200: 'Success'})
    def get(self, request, test_id):
        test_model = TestModel.objects.get(pk = test_id)
        res = {
            "msg" : "반환 성공",
            "data" : TestSerializer(test_model).data
        }
        
        return Response(res)