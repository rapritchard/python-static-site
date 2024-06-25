from textnode import TextNode
from inline_markdown import (extract_markdown_images, extract_markdown_links)

def main():
    text_node = TextNode("Hello, World!", "bold", "http://localhost:8888")
    
    #print(text_node)
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
    print(extract_markdown_images(text))
    
    text = "This is text with a [link](https://www.example.com)"
    print(extract_markdown_links(text))
    
main()