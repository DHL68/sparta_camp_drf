from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from product.models import Product as ProductModel

from product.serializers import ProductSerializer

from ai.permissions import IsAdminOrAuthenticatedReadOnly

from datetime import datetime

from django.db.models import Q

# Create your views here.

class ProductView(APIView):
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    
    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            Q(exposure_start_date__lte = today, exposure_end_date__gte = today,) |
            Q(user=request.user)
        )

        serializerd_data = ProductSerializer(products, many=True).data
        
        return Response(serializerd_data, status=status.HTTP_200_OK)
    
    #validator validator(입증하다) 설정
    def post(self, request):
        '''
        항상 유저의 값을 불러온다.
        user = request.user  때문에 이 구문은 필요가 없음
        request.user 의 정보를 request.data 의 user id 값에 넣어주는 과정
        '''
        request.data['user'] = request.user.id

        # product 의 serializer 데이터 값을 딕셔너리로 넘겨준다.
        product_serializer = ProductSerializer(data=request.data)

        # valid() 입증이 안되었을 경우 return False 로 넘겨준다. (검증과정)
        if product_serializer.is_valid():
            # validator 를 통과했을 경우 데이터 저장 / .is_valid() 가 통과가 되는 경우에만 저장 가능
            product_serializer.save()

            # return 으로 시리얼 데이터 보내주기
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        '''
        통과를 못한 경우
        .error 에는 validator에 실패한 필드와 실패 사유가 담겨 있다.
        '''
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, product_id):
        product = ProductModel.objects.get(id=product_id)
        '''
        위의 productmodels id 데이터를 시리얼로 불러오고 productserializer 로 다시 request.data 로 업데이트 한다.
        partial 는 일부 수정을 가능하게 해준다.
        '''
        product_serializer = ProductSerializer(product, data=request.data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()

            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)