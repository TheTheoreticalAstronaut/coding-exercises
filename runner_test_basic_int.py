import pytest

if __name__=="__main__":
    retcode = pytest.main(["--no-header", "--tb=no", "./tests/test_basic_int.py::TestBasicInt"])