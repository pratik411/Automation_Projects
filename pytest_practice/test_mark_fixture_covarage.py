import sys
import pytest


def test_abc():
    a = 2
    b = 3
    ans = a+b
    print ans


@pytest.mark.skipif(sys.platform == 'win32', reason="This feature is not supported on Windows")
def test_xyz():
    print "pratik"

ans = 4


@pytest.mark.skipif(ans == 5, reason="C value matched")
def test_aaa():
    print "Success"


