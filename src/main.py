import os
import shutil
from copy_static import (copy_files_recursive, public_dir)
                
def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print(f'{public_dir} directory deleted')
    
    print("Starting the directory copy process")
    copy_files_recursive()

if __name__ == '__main__':
    main()