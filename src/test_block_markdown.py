import unittest
from markdown_blocks import markdown_to_blocks

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
    

if __name__ == "__main__":
    unittest.main()