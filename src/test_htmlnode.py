import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Hello, World!", props={"href": "http://localhost:8888"})
        self.assertEqual(node.props_to_html(), 'href="http://localhost:8888"')
        
    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Hello, World!", props={"href": "http://localhost:8888", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="http://localhost:8888" target="_blank"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode("a", "Hello, World!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_repr(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, World!, None, {'class': 'greeting'})")
    
    def test_to_html(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p >Hello, World!</p>")
        
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
        
    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()