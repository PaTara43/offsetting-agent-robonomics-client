import typing as tp

from ast import literal_eval
from logging import getLogger


logger = getLogger(__name__)


def parse_income_message(raw_data: tp.List[tp.Any]) -> dict:
    """
    Parse income PubSub Message.

    :param raw_data: Income PubSub Message.

    :return: technics, amount, promisee, promisee_signature.

    """

    for i in range(len(raw_data)):
        raw_data[i] = chr(raw_data[i])
    data: str = "".join(raw_data)
    data_dict: tp.Dict[tp.Union[dict, int, str]] = literal_eval(data)

    return data_dict
