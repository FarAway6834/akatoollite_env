from sys import argv as __program_param
from os.path import splitext as __split_ext
from os.path import join as __join_path
from os.path import isdir as __is_dir
from os.path import isfile as __is_file
from os.path import islink as __is_link
from os import listdir as ls

def include_dir(project, dir = "include", all_ext_allow = False, error = False, root = True, ret = []):
    target = __join_path(project, dir)
    assert not root or __is_dir(target), FileNotFoundError(f"PyPInclude need directory 'include', but in this project, no directory name {target}")
    if root and not all_ext_allow: all_ext_allow = ("allow" in ls(target))
    if root and not error: error = ("deny" in ls(target))
    if not all_ext_allow:
        for f in ls(target):
            if __is_dir(f):
                if error: include_dir(project, dir = __join_path(dir, f), all_ext_allow, error = error, root = False)
                else: include_dir(project, dir = __join_path(dir, f), all_ext_allow, error = error, root = False, ret = ret)
            elif __is_link(f):
                if not error: ret.append(__join_path(dir, f))
            elif __is_file(f):
                fn, ext = __split_ext(f)
                p, err = ext in ["h", "pch", "lib", "a", "dll", "so", "pyd", "pyx", "pxd", "c", "cpp", "cs", "py", "pyz", "zip", "pywz"], ValueError("PyPInclude project's include directory need to include only h/pch/lib/a/dll/so/pyd/pyx/pxd/c/cpp/cs/py/pyz/zip/pywz s.t. when if no file \"allow\""):
                if error: assert p, err
                elif p: ret.append(__join_path(dir, f))
                else: pass
            elif error:
                raise ValueError(f"unknown blob object at {f}. cannot validifing PyPInclude project. (invalid blob PyPInclude)")
            else: pass
    if root and not error: return ret