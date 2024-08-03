import copy
from collections import OrderedDict

from util.api.exceptions import ServerFailure


def pop_items(validated_data: OrderedDict, items=None) -> OrderedDict:
    try:
        data = copy.deepcopy(validated_data)
        for item in list(data.keys()):
            if item in items:
                data.pop(item)
        return data
    except Exception as e:
        raise ServerFailure(detail="Ocorreu um erro ao remover os itens do validaded_data")
