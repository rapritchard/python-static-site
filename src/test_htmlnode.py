import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Hello, World!", props={"href": "http://localhost:8888"})
        self.assertEqual(node.props_to_html(), ' href="http://localhost:8888"')
        
    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Hello, World!", props={"href": "http://localhost:8888", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="http://localhost:8888" target="_blank"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode("a", "Hello, World!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_repr(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, World!, None, {'class': 'greeting'})")
    
    def test_to_html(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")
        
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
        
    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_parent(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello, World!"),
            LeafNode("p", "This is a ParentNode in action!"),
        ])
        self.assertEqual(
            node.to_html(), 
            "<div><p>Hello, World!</p><p>This is a ParentNode in action!</p></div>",
        )
    
    def test_paragraph(self):
        node = ParentNode("p", [
            LeafNode("b", "Hello, World!"),
            LeafNode(None, "This is a ParentNode in action!"),
            LeafNode("i", "Goodbye, World!"),
        ])
        self.assertEqual(
            node.to_html(), 
            "<p><b>Hello, World!</b>This is a ParentNode in action!<i>Goodbye, World!</i></p>",
        )
    
    def test_heading(self):
        node = ParentNode("h1", [
            LeafNode("b", "Hello, World!"),
            LeafNode(None, "This is a ParentNode in action!"),
            LeafNode("i", "Goodbye, World!"),
        ])
        self.assertEqual(
            node.to_html(),
            "<h1><b>Hello, World!</b>This is a ParentNode in action!<i>Goodbye, World!</i></h1>",
        )
    
    def test_to_html_parent_no_tag(self):
        node = ParentNode(None, [
            LeafNode("p", "Hello, World!"),
            LeafNode("p", "This is a ParentNode in action!"),
        ])
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()