import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def check_for_headings(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return True
    return False

def check_for_code(lines):
    return True if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```") else False

def check_for_quote(lines):
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def check_for_unordered_list(lines):
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True

def check_for_ordered_list(lines):
    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            return False
    return True

def block_to_block_type(block):
    lines = block.split("\n")

    if check_for_headings(block):
        return block_type_heading
    if check_for_code(lines):
        return block_type_code
    if check_for_quote(lines):
        return block_type_quote
    if check_for_unordered_list(lines):
        return block_type_unordered_list
    if check_for_ordered_list(lines):
        return block_type_ordered_list
    return block_type_paragraph

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())

    return filtered_blocks

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def heading_to_html_node(block):
    heading_count = block.count("#")
    if heading_count > 6:
        raise ValueError("Invalid markdown, heading level exceeds maximum of 6")
    heading_content = text_to_children(block[heading_count + 1:].strip())
    return ParentNode(f"h{heading_count}", heading_content)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))

def ulist_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        items.append(ParentNode("li", text_to_children(line[2:].strip())))
    return ParentNode("ul", items)

def olist_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        parts = re.split(r"(\d+\.)", line)
        items.append(ParentNode("li", text_to_children(parts[-1].strip())))
    return ParentNode("ol", items)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block incorrect format")
    text = block[4:-3]
    code = ParentNode("code", text_to_children(text))
    return ParentNode("pre", [code])

def blockquote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block, line does not start with '>'")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
            
    return ParentNode("blockquote", text_to_children(content))
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        html_node = None
        block_type = block_to_block_type(block)
        
        if block_type == block_type_heading:
            html_node = heading_to_html_node(block)
        elif block_type == block_type_unordered_list:
            html_node = ulist_to_html_node(block)
        elif block_type == block_type_ordered_list:
            html_node = olist_to_html_node(block)
        elif block_type == block_type_code:
            html_node = code_to_html_node(block)
        elif block_type == block_type_quote:
            html_node = blockquote_to_html_node(block)
        elif block_type == block_type_paragraph:
            html_node = paragraph_to_html_node(block)
        else:
            raise ValueError(f"Invalid block type: {block_type}")
        
        if html_node:
            html_nodes.append(html_node)
    
    return ParentNode("div", html_nodes, None)