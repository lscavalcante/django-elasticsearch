from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotFound

from shared.api.exceptions import ServerFailure


def get_or_none(classmodel, raise_exception=False, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        if raise_exception:
            raise ServerFailure(detail="Foi encontrado mais de um resultado no parametro de GET")
        return None
    except classmodel.DoesNotExist:
        if raise_exception:
            raise ServerFailure(detail=f"not found a result for {classmodel.__name__}")
        return None
    except ValueError as value_error:
        if raise_exception:
            raise ServerFailure(detail=f"{value_error}")
        return None
    except ValidationError as validation_error:
        if raise_exception:
            raise NotFound(detail=f"{validation_error.messages[0]}")
        return None
    except Exception as fatal_error:
        if raise_exception:
            raise ServerFailure(detail=f"Ocorreu um erro ao buscar o -  {classmodel.__name__}")
        return None
