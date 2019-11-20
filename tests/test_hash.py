import unittest

from tonggong.hash import Hash


class HashTestCase(unittest.TestCase):
    def test_md5(self):
        test_cases = [
            ('fc3ff98e8c6a0d3087d515c0473f8677', 'hello world!'),
            ('b8a14a625c0b404b4c0845fbf06374da', 'https://datarc.cn/'),
        ]
        for expected, case in test_cases:
            actual = Hash.md5(case)
            self.assertEqual(expected, actual)

    def test_sha1(self):
        test_cases = [
            ('430ce34d020724ed75a196dfc2ad67c77772d169', 'hello world!'),
            ('f34948571254aaa622c651c4a826ba65a223ca87', 'https://datarc.cn/'),
        ]
        for expected, case in test_cases:
            actual = Hash.sha1(case)
            self.assertEqual(expected, actual)

    def test_sha256(self):
        test_cases = [
            ('7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5e3df163be08e6ca9', 'hello world!'),
            ('9fcfd162cd418ba1c19c560c78ae238a2722a0f474dc4b8be3bef420490f777f', 'https://datarc.cn/'),
        ]
        for expected, case in test_cases:
            actual = Hash.sha256(case)
            self.assertEqual(expected, actual)
