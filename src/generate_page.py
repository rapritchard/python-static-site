import os
from pathlib import Path
from markdown_blocks import (markdown_to_html_node)

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:]
    raise ValueError('Title not found')
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating * {from_path} -> {dest_path} (Template: {template_path})")

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
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
        print(f'{dest_dir_path} directory created')
    
    if os.path.exists(dir_path_content):
        for item in os.listdir(dir_path_content):
            src_path = Path(dir_path_content, item)
            dest_path = Path(dest_dir_path, os.path.splitext(item)[0])
            print(f" * {src_path} -> {dest_path}")
            if os.path.isdir(src_path):
                generate_page_recursive(src_path, template_path, dest_path)
            elif os.path.isfile(src_path):
                generate_page(src_path, template_path, f"{dest_path}.html")