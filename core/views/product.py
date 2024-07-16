from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.product import Product
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.serializers.product import ProductListSerializer, ProductSerializer
from django.db.models import Count, Sum


class ProductList(APIView):
    def get(self, request):
        search_params = {}

        search_query = request.query_params.get("search")
        if search_query:
            search_params["search"] = search_query

        for field in [
            "name",
            "description",
            "category__name",
            "price",
            "availability",
            "status",
        ]:
            value = request.query_params.get(field)
            if value:
                search_params[field] = value

        ordering = request.query_params.get("ordering")
        if ordering:
            search_params["ordering"] = ordering

        products = Product.objects.search(**search_params)

        # Aggregate order counts for each product
        # products = (
        #     Product.objects.search(**search_params)
        #     .annotate(order_count=Count("variants__orderitem"))
        #     .filter(**search_params)
        #     .order_by("-order_count")
        # )  # Sort by most orders
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer)
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
