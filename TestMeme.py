import unittest
from typing import List
from Meme import Meme
from pyerr import (
    MsgTypeError,
    UrlTypeError
)


class TestMeme(unittest.TestCase):
    def setUp(self) -> None:
        self.correct_url: str = "www.multisoft.se"
        self.correct_msg: str = "1112031584"
        self.incorrect_msg: int = 1112031584
        self.incorrect_urls: List[str] = [
            "https://www.multisoft.se/",
            "https://www.multisoft.se",
            "http://www.multisoft.se/",
            "http://www.multisoft.se",
            "www.multisoft.com",
            "www.multisoft.com/",
            "www.multisoft.se/"
        ]

    def test_expected_url(self) -> None:
        meme = Meme(url=self.correct_url, msg=self.correct_msg)
        self.assertEqual(meme.url, "www.multisoft.se")

    def test_expected_msg(self) -> None:
        meme = Meme(url=self.correct_url, msg=self.correct_msg)
        self.assertEqual(meme.msg, "1112031584")

    def test_bad_msg(self) -> None:
        with self.assertRaises(MsgTypeError):
            Meme(url=self.correct_url, msg=self.incorrect_msg)

    def test_bad_url(self) -> None:
        for bad_url in self.incorrect_urls:
            with self.assertRaises(UrlTypeError):
                Meme(url=bad_url, msg=self.correct_msg)


if __name__ == '__main__':
    unittest.main()
