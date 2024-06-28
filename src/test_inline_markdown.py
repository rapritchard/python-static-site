import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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
        
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://test.com/image.png) and another ![second image](https://test.com/image2.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://test.com/image.png"),
                TextNode(" and another ", text_type_text),
                TextNode("second image", text_type_image, "https://test.com/image2.png"),
            ],
        )
        
    def test_split_nodes_image_single(self):
        node = TextNode(
            "![image](https://test.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("image", text_type_image, "https://test.com/image.png"),
            ],
        )
        
    def test_split_nodes_link(self):
        link_node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.example2.com)",
            text_type_text,
        )
        new_link_nodes = split_nodes_link([link_node])
        self.assertEqual(
            new_link_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and another ", text_type_text),
                TextNode("second link", text_type_link, "https://www.example2.com"),
            ],
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://test.com/image.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://test.com/image.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]
        )
    
    def test_text_to_textnodes_no_markdown(self):
        text = "This is text with no markdown"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is text with no markdown", text_type_text),
            ]
        )

if __name__ == "__main__":
    unittest.main()