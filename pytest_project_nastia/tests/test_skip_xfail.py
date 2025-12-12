import pytest
import sys
@pytest.mark.skip(reason="not yet")
def test_fut_feature(calc):
    assert calc.sub(10, 7) == 3

@pytest.mark.skipif(sys.platform == "win32", reason="we cant work at win32")
def test_only_non_win(calc):
    assert calc.div(8, 2) == 4

@pytest.mark.xfail(reason="known bug; division error")
def test_kmown_bug(calc):
    assert calc.div(10, 2) == 3
