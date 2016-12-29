import re
import unittest

from text_justify import justify

# Redefine constants rather than using the ones from text_justify.py so changes will be caught by the tests.
NEW_LINE = '\n'
SPACE = ' '


class TextJustifyTestCase(unittest.TestCase):

    def test_single_word_should_not_be_changed(self):
        input_ = 'somelongword'
        self.assertEqual(justify(input_, 30), input_)

    def test_multi_line(self):
        input_ = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Vestibulum sagittis dolor mauris, at elementum ligula tempor "
            "eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit "
            "amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu "
            "vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices "
            "nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum "
            "justo. Donec sed quam vel risus faucibus euismod. Suspendisse "
            "rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies "
            "a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac "
            "felis rhoncus pellentesque. Mauris at tellus enim. Aliquam "
            "eleifend tempus dapibus. Pellentesque commodo, nisi sit amet "
            "hendrerit fringilla, ante odio porta lacus, ut elementum justo "
            "nulla et dolor."
        )
        expected = NEW_LINE.join((
            "Lorem  ipsum  dolor  sit amet,",
            "consectetur  adipiscing  elit.",
            "Vestibulum    sagittis   dolor",
            "mauris,  at  elementum  ligula",
            "tempor  eget.  In quis rhoncus",
            "nunc,  at  aliquet orci. Fusce",
            "at   dolor   sit   amet  felis",
            "suscipit   tristique.   Nam  a",
            "imperdiet   tellus.  Nulla  eu",
            "vestibulum    urna.    Vivamus",
            "tincidunt  suscipit  enim, nec",
            "ultrices   nisi  volutpat  ac.",
            "Maecenas   sit   amet  lacinia",
            "arcu,  non dictum justo. Donec",
            "sed  quam  vel  risus faucibus",
            "euismod.  Suspendisse  rhoncus",
            "rhoncus  felis  at  fermentum.",
            "Donec lorem magna, ultricies a",
            "nunc    sit    amet,   blandit",
            "fringilla  nunc. In vestibulum",
            "velit    ac    felis   rhoncus",
            "pellentesque. Mauris at tellus",
            "enim.  Aliquam eleifend tempus",
            "dapibus. Pellentesque commodo,",
            "nisi    sit   amet   hendrerit",
            "fringilla,   ante  odio  porta",
            "lacus,   ut   elementum  justo",
            "nulla et dolor."
        ))
        self.assertEqual(justify(input_, 30), expected)

    # Tests below are redundants as all those have indirectly been tested
    # within `test_multi_line` but better express what is tested.

    def test_large_gaps_go_first(self):
        input_ = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Vestibulum sagittis dolor mauris, at elementum ligula tempor"
        )
        expected_gaps_lengths = (
            2, 2, 2, 1,  # 1st line
            2, 2,        # 2nd line
            4, 3,        # 3rd line
            2, 2, 2      # 4th line
        )

        justified_text = justify(input_, 30)
        gaps = re.findall(r' +', justified_text)
        gaps_lenghts = tuple(map(len, gaps))

        self.assertEqual(gaps_lenghts, expected_gaps_lengths)

    def test_lines_are_separated_with_new_line_characters(self):
        input_ = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Vestibulum sagittis dolor mauris, at elementum ligula tempor"
        )
        justified_text = justify(input_, 30)

        for i in range(30, len(input_), 31):
            self.assertEqual(justified_text[i], NEW_LINE)

    def test_lines_should_not_end_with_a_space(self):
        input_ = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Vestibulum sagittis dolor mauris, at elementum ligula tempor "
            "eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit "
            "amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu "
            "vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices "
            "nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum "
            "justo. Donec sed quam vel risus faucibus euismod. Suspendisse "
            "rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies "
            "a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac "
            "felis rhoncus pellentesque. Mauris at tellus enim. Aliquam "
            "eleifend tempus dapibus. Pellentesque commodo, nisi sit amet "
            "hendrerit fringilla, ante odio porta lacus, ut elementum justo "
            "nulla et dolor."
        )

        justified_text = justify(input_, 30)
        lines = justified_text.split(NEW_LINE)
        for line in lines:
            last_character = line[-1]
            self.assertIsNot(last_character, SPACE)

    def test_last_line_should_not_be_justified(self):
        input_ = "Lorem ipsum dolor sit amet, consectetur elit."
        expected_last_line = "consectetur elit."

        justified_text = justify(input_, 30)
        last_line = justified_text.split(NEW_LINE)[-1]

        self.assertEqual(last_line, expected_last_line)

    def test_last_line_should_not_contain_new_line_character(self):
        input_ = "Lorem ipsum dolor sit amet, consectetur elit."

        justified_text = justify(input_, 30)
        last_character = justified_text[-1]

        self.assertIsNot(last_character, NEW_LINE)
