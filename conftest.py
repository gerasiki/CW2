import pytest

from utils_dao import UtilsDAO


@pytest.fixture()
def utils_dao():
    utils_dao_instance = UtilsDAO()
    return utils_dao_instance
