import unittest
from inline_markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links)
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
        
    def test_extract_image(self):
        text = "This is text with an ![image](https://test.com/image.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://test.com/image.png")],
        )
    
    def test_extract_image_multiple(self):
        text = "This is text with an ![image](https://test.com/image.png) and ![image](https://test.com/image2.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://test.com/image.png"),
                ("image", "https://test.com/image2.png"),
            ],
        )
        
    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [("link", "https://www.example.com")],
        )
    
    def test_extract_link_multiple(self):
        text = "This is text with a [link](https://www.example.com) and [link](https://www.example2.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("link", "https://www.example2.com"),
            ],
        )

if __name__ == "__main__":
    unittest.main()