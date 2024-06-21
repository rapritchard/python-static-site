import unittest

from htmlnode import HTMLNode

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
        node = HTMLNode("a", "Hello, World!", props={"href": "http://localhost:8888"})
        self.assertEqual(repr(node), "HTMLNode(a, Hello, World!, None, {'href': 'http://localhost:8888'})")