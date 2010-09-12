"""
Minimal Unit Tests for Forrst API
"""


import unittest
import pyforrst

# This username will always exist ;)
TEST_USERNAME = "kyle"

# Matches above username
TEST_USERID = 1


class TestUserInfo(unittest.TestCase):
    """
    Test the user_info API function
    """

    def test_user_info_success(self):
        """
        Verify that user_info() returns correct data with valid username
        """
        user = pyforrst.user_info(TEST_USERNAME)
        self.assertTrue('username' in user, 'Username key not in return value')
        self.assertTrue('id' in user, 'ID key not in return value')
        self.assertEqual(user['username'], TEST_USERNAME,
                            "Username requested: '%s' returned: '%s'" % \
                            (TEST_USERNAME, user['username']))

        # int() conversions needed b/c forrst API returns unicode
        self.assertEqual(int(user['id']), TEST_USERID,
                         "User ID requested: %d returned: %d" % \
                         (TEST_USERID, int(user['id'])))

    def test_user_info_invalid_username(self):
        """
        Verify that user_info() returns an error when given invalid user
        """
        self.assertRaises(pyforrst.ForrstError, pyforrst.user_info,
                            'INVALIDUSER123')

if __name__ == '__main__':
    unittest.main()
