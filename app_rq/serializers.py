from rest_framework import serializers
from .models import Topics, Authors, Collections,Quote


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = '__all__'
class quoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'        
      


