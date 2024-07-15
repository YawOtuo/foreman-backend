from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth, ExtractYear


from django.shortcuts import get_object_or_404

from core.models.order import Order
from core.models.user import User


@api_view(["GET"])
def dashboard_api(request, user_id):
    user = get_object_or_404(User, id=user_id)

    current_year = datetime.now().year
    orders_by_month = (
        Order.objects.filter(user=user, created_at__year=current_year)
        .annotate(month=ExtractMonth("created_at"))
        .values("month")
        .annotate(total_orders=Count("id"))
        .order_by("month")
    )

    total_orders = Order.objects.filter(user=user).count()
    total_completed_orders = Order.objects.filter(user=user, status="delivered").count()
    total_cost_spent = (
        Order.objects.filter(user=user).aggregate(Sum("total_cost"))["total_cost__sum"]
        or 0
    )

    data = {
        "total_orders": total_orders,
        "total_completed_orders": total_completed_orders,
        "total_cost_spent": total_cost_spent,
        "orders_by_month": list(
            orders_by_month
        ),  # Convert QuerySet to list for JSON serialization
    }
    return Response(data)
