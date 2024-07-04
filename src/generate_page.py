import os
from markdown_blocks import (markdown_to_html_node)

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:]
    raise ValueError('Title not found')
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} -> {dest_path}, using:  {template_path}")

    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()
    
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    page_title = extract_title(markdown_content)
    
    final_page = template_content.replace('{{ Title }}', page_title).replace('{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_page)