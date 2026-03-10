
import pytest
import logging
from app import login,add_product,apply_discount,payment

logger=logging.getLogger(__name__)


@pytest.fixture
def sample_amount():
    return 100


@pytest.mark.parametrize("price,qty,result",[
(10,2,20),
(5,5,25),
(100,1,100)
])
def test_add_product(price,qty,result):

    logger.info("Testing add product")

    assert add_product(price,qty)==result


def test_login_success():

    assert login("admin","admin123")==True


def test_login_fail():

    with pytest.raises(Exception):
        login("admin","wrong")


def test_discount(sample_amount):

    assert apply_discount(sample_amount)==90


def test_payment():

    assert payment(100)=="Payment Successful"
