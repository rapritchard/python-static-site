import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "http://localhost:8888")
        node2 = TextNode("This is a text node", text_type_text, "http://localhost:8888")
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "http://localhost:8888")
        self.assertEqual(repr(node), "TextNode(This is a text node, text, http://localhost:8888)")
        
    


if __name__ == "__main__":
    unittest.main()