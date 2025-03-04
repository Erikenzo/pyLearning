import twttr
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "twttr"
    assert shorten("Erikas") == "rks"
    assert shorten("Mano Namas") == "mn nms"