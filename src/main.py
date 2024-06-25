from textnode import (TextNode, split_nodes_delimiter, text_type_text, text_type_code)

def main():
    text_node = TextNode("Hello, World!", "bold", "http://localhost:8888")
    
    print(text_node)
    
main()