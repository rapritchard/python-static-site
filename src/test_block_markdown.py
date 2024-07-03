import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    markdown_to_html_node
)
from htmlnode import HTMLNode

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                'This is **bolded** paragraph', 
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                '* This is a list\n* with items'
            ]
        )
        
    def test_markdown_to_blocks_excessive_newlines(self):
        markdown = """
This is **bolded** paragraph



This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                'This is **bolded** paragraph', 
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                '* This is a list\n* with items'
            ]
        )
    
    def test_markdown_to_blocks_empty(self):
        markdown = ''
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [])
        
    def test_block_to_block_type(self):
        block = 'This is a paragraph'
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = '# This is a heading'
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = '>This is a quote\n>with multiple lines\n>and multiple paragraphs'
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = '>This is a quote\n> with multiple lines\nand multiple paragraphs'
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = '* this is a list\n* with multiple items'
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = '- this is a list\n- with multiple items'
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = '- this is a list\nwith multiple items'
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = '1. this is a list\n2. with multiple items'
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
        
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
        
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
        
    
if __name__ == "__main__":
    unittest.main()