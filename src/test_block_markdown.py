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
)

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
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [])
        
    def test_block_to_block_type(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = ">This is a quote\n>with multiple lines\n>and multiple paragraphs"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = ">This is a quote\n> with multiple lines\nand multiple paragraphs"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "* this is a list\n* with multiple items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "- this is a list\n- with multiple items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "- this is a list\nwith multiple items"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "1. this is a list\n2. with multiple items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
    



if __name__ == "__main__":
    unittest.main()