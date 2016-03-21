from unittest import TestCase, main
from unittest.mock import Mock
from check_for_duplicates import omit_this


class CheckForDuplicatesTest(TestCase):

    def test_omit_this(self):
        info = Mock(response_code=200)
        response_code = 302
        assert(omit_this(info, response_code))

    def test_omit_this_false(self):
        info = Mock(response_code=200)
        response_code = 200
        self.assertFalse(omit_this(info, response_code))

    def test_omit_this_false_not_interested(self):
        info = Mock(response_code=200)
        response_code = None
        self.assertFalse(omit_this(info, response_code))


if __name__ == '__main__':
    main()
