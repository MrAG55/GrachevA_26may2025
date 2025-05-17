
import requests
import pytest
from utils import test_data

headers = {"Content-Type": "application/json"}


@pytest.mark.api
@pytest.mark.parametrize("action", ["add", "change", "delete"])
def test_cart_actions(action):
    payload = {
        "idCookie": test_data.id_cookie,
        "idProd": test_data.product_id,
        "type": action
    }

    response = requests.post(test_data.api_url, json=payload, headers=headers)

    assert response.status_code == 200, (f"Ошибка при"
                                         f" '{action}': {response.text}")
