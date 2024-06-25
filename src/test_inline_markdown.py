import unittest
from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_bold(self):
        nodes = [TextNode("This is a **bold** word", text_type_text)]
        new_nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )
    
    def test_split_italic(self):
        nodes = [TextNode("This is a *italic* word", text_type_text)]
        new_nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
        )
        
    def test_split_code(self):
        nodes = [TextNode("This is a `code` word", text_type_text)]
        new_nodes = split_nodes_delimiter(nodes, "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" word", text_type_text),
            ],
        )
        
    def test_bold_multiple(self):
        nodes = [TextNode("This is a **bold** and **bold** word", text_type_text)]
        new_nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )
        
    def test_bold_and_italic(self):
        nodes = [TextNode("This is a **bold** and *italic* word", text_type_text)]
        new_nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
        )

if __name__ == "__main__":
    unittest.main()