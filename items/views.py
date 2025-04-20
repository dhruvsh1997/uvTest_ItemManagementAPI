from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET','POST'])              # wrap as DRF view :contentReference[oaicite:5]{index=5}
def item_list(request):
    # --- GET: list or filter items ---
    if request.method == 'GET':
        # 1. Check for query params
        pk       = request.GET.get('itemID')            # get itemID if provided :contentReference[oaicite:6]{index=6}
        day      = request.GET.get('day')
        month    = request.GET.get('month')
        year     = request.GET.get('year')
        name     = request.GET.get('itemName')

        if pk:
            # 2. Fetch single item by ID
            try:
                item = Item.objects.get(itemID=pk)
                serializer = ItemSerializer(item)
                return Response(serializer.data)
            except Item.DoesNotExist:
                return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # 3. Otherwise, build filter dict
        filters = {}
        if day:   filters['day']   = int(day)
        if month: filters['month'] = int(month)
        if year:  filters['year']  = int(year)
        if name:  filters['itemName__icontains'] = name

        # 4. Apply filters
        items = Item.objects.filter(**filters) if filters else Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


    # --- POST: create new item ---
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   # creation status :contentReference[oaicite:7]{index=7}
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def item_detail(request, pk):
    # 1. Try to fetch the item
    try:
        item = Item.objects.get(itemID=pk)
    except Item.DoesNotExist:
        return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)

    # 2. GET single item
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    # 3. PUT update
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. DELETE
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                    # no content status :contentReference[oaicite:8]{index=8}

