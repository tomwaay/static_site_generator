import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_types(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is not text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is not text node", "bold", None)
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()