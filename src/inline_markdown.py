import re
from textnode import (TextNode, text_type_text, text_type_image, text_type_link, text_type_code, text_type_italic, text_type_bold)

def text_to_textnodes(text):
    new_nodes = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section is not closed")
        
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, text_type_text))
            else:
                new_nodes.append(TextNode(part, text_type))
        
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        images = extract_markdown_images(remaining_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            parts = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, image is not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            remaining_text = parts[1]
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, text_type_text))
        
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        links = extract_markdown_links(remaining_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            parts = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, link is not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            remaining_text = parts[1]
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, text_type_text))
        
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)