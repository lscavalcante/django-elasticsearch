from rest_framework.serializers import Serializer


def update_fields(instance: object, serializer: Serializer, fields: list[str]) -> None:
    for field in fields:
        if field in serializer.validated_data:
            setattr(instance, field, serializer.validated_data[field])
