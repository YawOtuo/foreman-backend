# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from core.models.order import Order, OrderItem
from core.models.product import Product
from core.models.productvariant import ProductVariant
from core.models.shippingaddress import ShippingAddress
from core.models.user import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.serializers.order import OrderDetailSerializer, OrderListSerializer


class OrderListAPI(APIView):
    """
    API view to handle listing and creating orders.
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="List of orders", schema=OrderListSerializer(many=True)
            ),
            404: "Orders not found",
        }
    )
    def get(self, request, user_id):
        """
        List all orders for the specified user.
        """
        # Verify user existence
        user = get_object_or_404(User, id=user_id)

        # Filter orders by user
        orders = Order.objects.filter(user=user)

        if not orders.exists():
            return Response([], status=status.HTTP_200_OK)

        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "total_order_cost": openapi.Schema(
                    type=openapi.TYPE_NUMBER, description="Total cost of the order"
                ),
                "total_order_quantity": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Total quantity of items in the order",
                ),
                "order_items": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "product_id": openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="ID of the product to add to order",
                            ),
                            "quantity": openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="Quantity of the product",
                            ),
                            "totalCost": openapi.Schema(
                                type=openapi.TYPE_NUMBER,
                                description="Total cost of this item",
                            ),
                        },
                        required=["product_id", "quantity", "totalCost"],
                    ),
                ),
                "shipping_address": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "address_line_1": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Address line 1"
                        ),
                        "address_line_2": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Address line 2",
                            nullable=True,
                        ),
                        "city": openapi.Schema(
                            type=openapi.TYPE_STRING, description="City"
                        ),
                        "state": openapi.Schema(
                            type=openapi.TYPE_STRING, description="State", nullable=True
                        ),
                        "postal_code": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Postal code",
                            nullable=True,
                        ),
                        "country": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Country",
                            default="Ghana",
                        ),
                        "is_default": openapi.Schema(
                            type=openapi.TYPE_BOOLEAN, description="Is default address"
                        ),
                    },
                    required=["address_line_1", "city", "country"],
                ),
            },
            required=["total_order_cost", "total_order_quantity", "order_items", "shipping_address"],
        ),
        responses={
            201: openapi.Response(
                description="Order created", schema=OrderListSerializer
            ),
            400: "Bad Request",
        },
    )
    def post(self, request, user_id):
        """
        Create a new order for the specified user.
        """
        data = request.data
        total_order_cost = data.get("total_order_cost")
        total_order_quantity = data.get("total_order_quantity")
        order_items_data = data.get("order_items")
        shipping_address_data = data.get("shipping_address")

        if (
            not total_order_cost
            or not total_order_quantity
            or not order_items_data
            # or not shipping_address_data
        ):
            return Response(
                {"message": "Incomplete order data provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = get_object_or_404(User, id=user_id)

        # Validate all products exist before creating any order items
        products_exist = True
        for item_data in order_items_data:
            product_id = item_data.get("product_id")
            product = get_object_or_404(ProductVariant, id=product_id)
            if not product:
                products_exist = False
                break

        if not products_exist:
            return Response(
                {"message": "One or more products variants do not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Retrieve or create the shipping address
        # shipping_address, created = ShippingAddress.objects.get_or_create(
        #     user=user,
        #     address_line_1=shipping_address_data.get("address_line_1"),
        #     address_line_2=shipping_address_data.get("address_line_2"),
        #     city=shipping_address_data.get("city"),
        #     state=shipping_address_data.get("state"),
        #     postal_code=shipping_address_data.get("postal_code"),
        #     country=shipping_address_data.get("country", "Ghana"),
        #     is_default=shipping_address_data.get("is_default", False),
        # )

        # Create the order
        order = Order.objects.create(
            user=user,
            total_cost=total_order_cost,
            total_quantity=total_order_quantity,
            # shipping_address=shipping_address,
        )

        order_items = []
        for item_data in order_items_data:
            product_id = item_data.get("product_id")
            quantity = item_data.get("quantity")
            totalCost = item_data.get("totalCost")

            # Create OrderItem and link to order
            order_item = OrderItem.objects.create(
                order=order,
                product_variant_id=product_id,
                quantity=quantity,
                total_cost=totalCost,
            )
            order_items.append(order_item)

        # Serialize the order and return the response
        serializer = OrderListSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailAPI(APIView):
    """
    API view to handle retrieving, updating, and deleting individual orders.
    """

    @swagger_auto_schema(
        operation_id="GetOrderDetail",  # Custom operation ID
        responses={
            200: openapi.Response(
                description="Order details", schema=OrderDetailSerializer
            ),
            404: "Order not found",
        },
    )
    def get(self, request, order_id, user_id):
        """
        Retrieve an order by its ID.
        """
        user = get_object_or_404(User, id=user_id)

        order = get_object_or_404(Order, id=order_id, user=user)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "is_paid": openapi.Schema(
                    type=openapi.TYPE_BOOLEAN, description="Payment status of the order"
                ),
            },
            required=["is_paid"],
        ),
        responses={
            200: openapi.Response(
                description="Order updated", schema=OrderDetailSerializer
            ),
            400: "Bad Request",
            404: "Order not found",
        },
    )
    def put(self, request, order_id, user_id):
        """
        Update an order's details.
        """
        user = get_object_or_404(User, id=user_id)

        order = get_object_or_404(Order, id=order_id, user=user)
        serializer = OrderDetailSerializer(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Order updated successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: "Order deleted",
            404: "Order not found",
        }
    )
    def delete(self, request, order_id, user_id):
        """
        Delete an order by its ID.
        """
        user = get_object_or_404(User, id=user_id)

        order = get_object_or_404(Order, id=order_id, user=user)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
