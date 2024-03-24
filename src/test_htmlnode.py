import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode()
        print(node)

    def test_props_to_html(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
        print(node.props_to_html())

    def test_more_props_to_html(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank","href2": "https://www.google.com", "target2": "_blank"})
        print(node.props_to_html())
    


if __name__ == "__main__":
    unittest.main()