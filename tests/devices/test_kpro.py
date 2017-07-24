from unittest import TestCase

from devices import *

class TestKpro(TestCase):

    def test_rpm(self):
        self.assertEqual(Kpro.rpm(), 1)
        self.assertEqual(1, 1)
