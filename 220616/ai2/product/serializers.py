from rest_framework import serializers
from product.models import Product as ProductModel

class ProductSerializer(serializers.ModelSerializer):
    '''
    조회 시 표기되는 id 값에 대한 노출 타입 변경 ( id 값 에서 > 유저의 이름으로)
    이름 말고도 유저가 저장한 데이터 필드를 입력하면 노출시킬 수 있음
    '''
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


    class Meta:
        model = ProductModel
        # Product field 설정
        fields = [
            'user', 'title', 'thumbnail', 'description',
            'created', 'exposure_start_date', 'exposure_end_date',
            ]