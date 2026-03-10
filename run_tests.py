
import pytest
from optimizer import prioritize_tests

tests=prioritize_tests()

print("Optimized Tests:",tests)

if tests:
    pytest.main(["-v"] + tests)
else:
    pytest.main(["-v"])
