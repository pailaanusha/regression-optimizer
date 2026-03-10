
from optimizer import prioritize_tests

def test_optimizer():

    tests=prioritize_tests()

    assert isinstance(tests,list)
