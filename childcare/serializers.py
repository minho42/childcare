from rest_framework import serializers
from .models import Childcare
from core.utils import get_all_fields_except


class ChildcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childcare
        # fields = "__all__"
        fields = get_all_fields_except(
            Childcare,
            [
                "created",
                "modified",
                "approval_number",
            ],
        )
