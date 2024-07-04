import os
import shutil

def copy_files_recursive(src_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        print(f'{target_dir} directory created')
    
    if os.path.exists(src_dir):
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(target_dir, item)
            
            if os.path.isdir(src_path):
                copy_files_recursive(src_path, dest_path)
            elif os.path.isfile(src_path):
                print(f' * {src_path} -> {dest_path}')
                shutil.copy(src_path, dest_path)
    else:
        raise FileNotFoundError(f'{src_dir} directory does not exist')