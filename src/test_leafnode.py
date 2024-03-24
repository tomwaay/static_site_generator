import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p","This is a paragraph of text.")
        print(node.to_html())

    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.to_html())
        

if __name__ == "__main__":
    unittest.main()