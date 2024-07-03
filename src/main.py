from textnode import TextNode
from markdown_blocks import markdown_to_html_node
def main():
    text_node = TextNode("Hello, World!", "bold", "http://localhost:8888")
    
    print(text_node)
 
main()