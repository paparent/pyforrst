"""
Minimal Unit Tests for Forrst API
"""


import unittest
import pyforrst

# This username will always exist ;)
TEST_USERNAME = "kyle"

# Matches above username
TEST_USERID = u'1'


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

        self.assertEqual(user['id'], TEST_USERID,
                         "User ID requested: %s returned: %s" % \
                         (TEST_USERID, user['id']))

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
        # int() conversion needed b/c API takes int, not unicode
        self._verify_test_user(pyforrst.user_info_by_id(int(TEST_USERID)))

    def test_user_info_id_invalid_id(self):
        """
        Verify that user_info_by_id() returns an error when given invalid id
        """
        self.assertRaises(pyforrst.ForrstError, pyforrst.user_info_by_id, -1)


class TestUserPosts(unittest.TestCase):
    """
    Test user_posts API function
    """

    def _verify_posts_from_user(self, user, posts):
        """
        Helper method to verify posts for given user
        """

        for post in posts:
            # Don't bother testing for EVERY key, just the 'important' ones
            self.assertTrue('id' in post, "ID key missing from posts")
            self.assertTrue('content' in post, "Content key missing from post")
            self.assertTrue('user_id' in post, "User ID key missing from post")

            self.assertEqual(post['user_id'], TEST_USERID,
                         "Post's User ID: %s doesn't match requested: %s" % \
                         (post['user_id'], TEST_USERID))

    def test_user_posts_success(self):
        """
        Verify user_posts returns correct data for valid user
        """
        self._verify_posts_from_user(TEST_USERNAME, pyforrst.user_posts(TEST_USERNAME))


    def test_user_posts_invalid_user(self):
        """
        Verify user_posts returns error when given invalid username
        """
        self.assertRaises(pyforrst.ForrstError, pyforrst.user_posts,
                            'INVALIDUSER123')


if __name__ == '__main__':
    unittest.main()
