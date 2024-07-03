from textnode import TextNode
from markdown_blocks import markdown_to_html_node
def main():
    text_node = TextNode("Hello, World!", "bold", "http://localhost:8888")
    
    print(text_node)
    
    markdown = """
# Heading 1

This is a paragraph.

* Bullet point 1
* Bullet point 2

> This is a quote block.
> This is a quote block as well.

## Heading 2

This is another paragraph.

1. Ordered item 1
2. Ordered item 2

```
print('Hello, World!')
```
"""
    html_nodes = markdown_to_html_node(markdown)
    print(html_nodes)
 
main()