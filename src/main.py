import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "/home/wince/workspace/github.com/Wince90/static_site_generator/static/"
dir_path_public = "/home/wince/workspace/github.com/Wince90/static_site_generator/public/"
dir_path_content = "/home/wince/workspace/github.com/Wince90/static_site_generator/content/"
template_path = "/home/wince/workspace/github.com/Wince90/static_site_generator/template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()