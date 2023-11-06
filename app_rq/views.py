from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import Quote,Topics,Collections,Authors,Featured
import random
from .serializers import TopicSerializer,AuthorSerializer,CollectionSerializer,quoteSerializer
from main_django.settings import database_name,mongodb_connection
# MongoDB connection parameters
mongo_uri = mongodb_connection
database_name = database_name

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def Topicsdata(request, topic_name):
    try:
        # Establish a connection to MongoDB
        client = MongoClient(mongo_uri)

        # Select the appropriate database and collection
        db = client[database_name]
        collection = db.topicdata

        # Create a projection to include the specified field dynamically
        projection = {topic_name: 1}

        # Query the database to retrieve data based on the field name
        result = collection.find_one({}, projection)

        if result:
            # Remove the '_id' field from the result as it can't be serialized to JSON
            result.pop('_id', None)
            return JsonResponse(result)
        else:
            return JsonResponse({"error": "Field not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def Authorsdata(request, author_name):
    try:
        # Establish a connection to MongoDB
        client = MongoClient(mongo_uri)

        # Select the appropriate database and collection
        db = client[database_name]
        collection = db.authordata

        # Create a projection to include the specified field dynamically
        projection = {author_name: 1}

        # Query the database to retrieve data based on the field name
        result = collection.find_one({}, projection)

        if result:
            # Remove the '_id' field from the result as it can't be serialized to JSON
            result.pop('_id', None)
            return JsonResponse(result)
        else:
            return JsonResponse({"error": "Field not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def Collectionsdata(request, collection_name):
    try:
        # Establish a connection to MongoDB
        client = MongoClient(mongo_uri)

        # Select the appropriate database and collection
        db = client[database_name]
        collection = db.collectiondata

        # Create a projection to include the specified field dynamically
        projection = {collection_name: 1}

        # Query the database to retrieve data based on the field name
        result = collection.find_one({}, projection)

        if result:
            # Remove the '_id' field from the result as it can't be serialized to JSON
            result.pop('_id', None)
            return JsonResponse(result)
        else:
            return JsonResponse({"error": "Field not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def topics(request):
    topics = Topics.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def authors(request):
    authors = Authors.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def collections(request):
    collections = Collections.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def Home(request):
    quotes = list(Quote.objects.values('author', 'quote','image_url'))
    featured_data = Featured.objects.values('featured').first()  
    
    if featured_data:
        featured_list = featured_data['featured']
        random.shuffle(featured_list)
        featured_three_topics = random.sample(featured_list, 3)
    
    random.shuffle(quotes)
    selected_quotes = quotes[:13]
    
    response_data = {
        'Featured': featured_three_topics,
        'Quotes': selected_quotes
        
    }
    return JsonResponse(response_data, safe=False)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def quote(request):
    quotes = Quote.objects.all()
    quotes_list = list(quotes)  
    random.shuffle(quotes_list)
    selected_quotes = quotes_list[:10]
    serializer = quoteSerializer(selected_quotes, many=True)
    return Response(serializer.data)
   



