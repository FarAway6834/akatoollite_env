from sys import argv as __program_param
from os.path import splitext as __split_ext
from os.path import join as __join_path
from os.path import isdir as __is_dir
from os.path import isfile as __is_file
from os.path import islink as __is_link
from os import listdir as ls

def include_dir(dir, all_ext_allow = False, root = True):
    assert not root or __is_dir(dir), FileNotFoundError(f"PyPInclude need directory 'include', but in this project, no directory name {dir}")
    if not all_ext_allow:
        for f in ls(dir):
            if __is_dir(f): include_dir(__join_path(dir, f))
            elif __is_link(f): pass
            elif __is_file(f):
                fn, ext = __split_ext(f)
                if ext in ["h", "pch", "lib", "a", "dll", "so", "pyd", "pyx", "pxd"0
            else:
                raise ValueError(f"unknown blob object at {f}. cannot validifing PyPInclude project. (invalid blob PyPInclude)")