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

    def _verify_test_user(self, user):
        """
        Helper method for verifying user data against test user as defined by
        TEST_USERNAME and TEST_USERID
        """
        self.assertTrue('username' in user, 'Username key not in return value')
        self.assertTrue('id' in user, 'ID key not in return value')
        self.assertEqual(user['username'], TEST_USERNAME,
                            "Username requested: '%s' returned: '%s'" % \
                            (TEST_USERNAME, user['username']))

        # int() conversions needed b/c forrst API returns unicode
        self.assertEqual(int(user['id']), TEST_USERID,
                         "User ID requested: %d returned: %d" % \
                         (TEST_USERID, int(user['id'])))

    def test_user_info_success(self):
        """
        Verify that user_info() returns correct data with valid username
        """
        self._verify_test_user(pyforrst.user_info(TEST_USERNAME))

    def test_user_info_invalid_username(self):
        """
        Verify that user_info() returns an error when given invalid user
        """
        self.assertRaises(pyforrst.ForrstError, pyforrst.user_info,
                            'INVALIDUSER123')

    def test_user_info_id_success(self):
        """
        Verify that user_info_by_id() returns correct data with valid user id
        """
        self._verify_test_user(pyforrst.user_info_by_id(TEST_USERID))

    def test_user_info_id_invalid_id(self):
        """
        Verify that user_info_by_id() returns an error when given invalid id
        """
        self.assertRaises(pyforrst.ForrstError, pyforrst.user_info_by_id, -1)


if __name__ == '__main__':
    unittest.main()
