import pytest


# strict=True show in report that test should be failed but was passed
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail()
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
