import os
import shutil
from copy_static import copy_files_recursive
from generate_page import generate_page

default_content_dir = 'content/'
default_public_dir = 'public/'
default_base_dir = 'static/'
                
def main():
    if os.path.exists(default_public_dir):
        shutil.rmtree(default_public_dir)
        print(f'{default_public_dir} directory deleted')
    
    print("Starting the directory copy process")
    copy_files_recursive(default_base_dir, default_public_dir)
    generate_page(f'{default_content_dir}index.md', 'template.html', f'{default_public_dir}index.html')

if __name__ == '__main__':
    main()