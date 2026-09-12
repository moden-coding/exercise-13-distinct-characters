#!/usr/bin/env python3

import random
import string
import unittest

from src.distinct_characters import distinct_characters


def random_words(count, length):
    """Generate `count` random uppercase words of the given length."""
    words = []
    for _ in range(count):
        letters = [random.choice(string.ascii_uppercase) for _ in range(length)]
        words.append("".join(letters))
    return words


class TestDistinctCharacters(unittest.TestCase):

    def test_worked_example(self):
        words = ["check", "look", "try", "pop"]
        result = distinct_characters(words)
        self.assertIsInstance(
            result, dict,
            msg=f"distinct_characters should return a dictionary. Got {type(result)}.")
        self.assertEqual(
            result["check"], 4,
            msg="'check' has letters c,h,e,c,k -> 4 distinct characters "
            "('c' repeats), not 5.")
        self.assertEqual(
            result["look"], 3,
            msg="'look' has letters l,o,o,k -> 3 distinct characters "
            "('o' repeats), not 4.")
        self.assertEqual(
            result["try"], 3,
            msg="'try' has 3 distinct letters and none repeat.")
        self.assertEqual(
            result["pop"], 2,
            msg="'pop' has letters p,o,p -> 2 distinct characters "
            "('p' repeats), not 3.")

    def test_empty_list(self):
        result = distinct_characters([])
        self.assertEqual(
            len(result), 0,
            msg="distinct_characters([]) should be an empty dictionary, "
            "since there are no words to count.")

    def test_word_with_all_repeated_characters(self):
        result = distinct_characters(["aaaa"])
        self.assertEqual(
            result["aaaa"], 1,
            msg="'aaaa' is a single character repeated four times, so it "
            "has only 1 distinct character, not 4.")

    def test_word_with_no_repeats(self):
        result = distinct_characters(["abcdef"])
        self.assertEqual(
            result["abcdef"], 6,
            msg="'abcdef' has 6 different letters and none repeat, so the "
            "distinct count should be 6.")

    def test_random_words(self):
        words = random_words(20, 12)
        result = distinct_characters(words)
        self.assertEqual(
            len(result), len(set(words)),
            msg="The result should have exactly one entry per distinct "
            "word in the input list.")
        for word in words:
            self.assertEqual(
                result[word], len(set(word)),
                msg="Number of distinct characters of word '%s' was "
                "incorrect!" % word)


if __name__ == '__main__':
    unittest.main()
