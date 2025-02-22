
from botclient.botclient import Bot
from botclient.textbot import TextBot
from botclient.picturebot import PictureBot

def test_init():
    b = Bot()
    assert b

def test_textbot():
    b = TextBot()
    assert b

def test_picturebot():
    b = PictureBot()
    assert b