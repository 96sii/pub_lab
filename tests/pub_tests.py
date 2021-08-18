import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Queen's left arm")

    def test_pub_has_name(self):
        self.assertEqual("The Queen's left arm", self.pub.name)