from exercises import lists

class TestLists:
    def test_empty_list(self):
        list_input = []
        list_output = []
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_one_element_lowercase(self):
        list_input = ["hello"]
        list_output = ["hello"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_one_element_general(self):
        list_input = ["HeLlo fRom 2022"]
        list_output = ["hello from 2022"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_0(self):
        list_input = ["hello", "juice", "World", "fantasy", "joke"]
        list_output = ["fantasy", "hello", "joke", "juice", "world"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_1(self):
        list_input = ["aaa", "AaA"]
        list_output = ["aaa", "aaa"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_2(self):
        list_input = ["helLo WOrld", "HELLO"]
        list_output = ["hello", "hello world"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_3(self):
        list_input = ["juMpynEss", "JUMP", "jumpy"]
        list_output = ["jump", "jumpy", "jumpyness"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_4(self):
        list_input = ["Q", "w", "e", "R", "t", "y", "u", "I", "O", "p", "A", "s", "D", "F",
                        "g", "h", "J", "k", "l", "z", "X", "c", "V", "b", "N", "M"]
        list_output = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_5(self):
        list_input = [" A", "A", "A "]
        list_output = [" a", "a", "a "]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_words_6(self):
        list_input = [" ", ""]
        list_output = ["", " "]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_0(self):
        list_input = ["234", "345", "123"]
        list_output = ["123", "234", "345"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_1(self):
        list_input = ["1000", "2"]
        list_output = ["1000", "2"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_2(self):
        list_input = ["5", "2", "3", "9", "0", "7", "6", "1", "4", "8"]
        list_output = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_3(self):
        list_input = ["77 7", "777"]
        list_output = ["77 7", "777"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_4(self):
        list_input = ["99328", "", "1763", "6542"]
        list_output = ["", "1763", "6542", "99328"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_numbers_5(self):
        list_input = ["763 24", "8732 332", "3", "74 211", "84 2", "81", "129 231", "8873", "093", "00 1", "1902", "56122 992", "166", "16"]
        list_output = ["00 1", "093", "129 231", "16", "166", "1902", "3", "56122 992", "74 211", "763 24", "81", "84 2", "8732 332", "8873"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_general_0(self):
        list_input = ["56", "woRLD  ", " 56", "hEllo", "", "HELLO", " "]
        list_output = ["", " ", " 56", "56", "hello", "hello", "world  "]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_general_1(self):
        list_input = ["RanD0m", "random", "1 rAndom", "Rand00m", " ranDOM", "RANDOM  ", "RANdom 8"]
        list_output = [" random", "1 random", "rand00m", "rand0m", "random", "random  ", "random 8"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_general_2(self):
        list_input = ["Q", "8", "w", "3", "e", "R", "t", "4", "y", "u", "0", "I", "O", "p", "", "A", "s", "9","D", "F",
                        "g", "h", " ", "J", "1", "2", "k", "l", "5", "z", "X", "c", "V", "b", "6", "N", "7", "M"]
        list_output = ["", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h",
                        "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_general_3(self):
        list_input = ["65abc", " Hi THERE", "HI there", "88 birds", "hOly c0W", "Mega H1ts"]
        list_output = [" hi there", "65abc", "88 birds", "hi there", "holy c0w", "mega h1ts"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def test_multiple_elements_general_4(self):
        list_input = ["There were 55 bottles in there", "I do not care about it", "Only 6 left", "That is great",
                        "Alex called her mom yesterday", "30 pancakes will do", "He really exceeded himself this time",
                        "Richard said he would come", "Zebras are pretty smart as far as I know", "Good job"]
        list_output = ["30 pancakes will do", "alex called her mom yesterday", "good job", "he really exceeded himself this time",
                        "i do not care about it", "only 6 left", "richard said he would come", "that is great",
                        "there were 55 bottles in there", "zebras are pretty smart as far as i know"]
        list = lists.sort_strings_lowercase(list_input)
        assert list_output == list, self._assert_fail_value_str(list_output, list)

    def _assert_fail_value_str(self, expected: int, found: int) -> str:
        return "Unexpected value: expected {0}, found {1}".format(expected, found)
