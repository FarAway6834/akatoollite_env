from sys import argv as __program_param
from os.path import splitext as __split_ext
from os.path import join as __join_path
from os.path import isdir as __is_dir
from os.path import isfile as __is_file
from os.path import islink as __is_link
from os.path import dirname as __get_dir
from os import listdir as ls

def PyPInclude(project, dir = "include", all_ext_allow = False, error = False, root = True, ret = []):
    target = __join_path(project, dir)
    assert not root or __is_dir(target), FileNotFoundError(f"PyPInclude need directory 'include', but in this project, no directory name {target}")
    if root and not all_ext_allow: all_ext_allow = ("allow" in ls(target))
    if root and not error: error = ("deny" in ls(target))
    if not all_ext_allow:
        for f in ls(target):
            if __is_dir(f):
                if error: PyPInclude(project, dir = __join_path(dir, f), all_ext_allow, error = error, root = False)
                else: PyPInclude(project, dir = __join_path(dir, f), all_ext_allow, error = error, root = False, ret = ret)
            elif __is_link(f):
                if not error: ret.append(__join_path(dir, f))
            elif __is_file(f):
                fn, ext = __split_ext(f)
                p, err = ext in ["h", "pch", "lib", "a", "dll", "so", "pyd", "pyx", "pxd", "c", "cpp", "cs", "py", "pyz", "zip", "pywz"], ValueError("PyPInclude project's include directory need to include only h/pch/lib/a/dll/so/pyd/pyx/pxd/c/cpp/cs/py/pyz/zip/pywz s.t. when if no file \"allow\". (invalid blob PyPInclude)"):
                if error: assert p, err
                elif p: ret.append(__join_path(dir, f))
                else: pass
            elif error:
                raise ValueError(f"unknown blob object at {f}. cannot validifing PyPInclude project. (invalid blob PyPInclude)")
            else: pass
    if root and not error: return "\n".join(map("include {}".format, ret))

def main():
    pkg = __program_param[1]
    ls_pkg = ls(pkg)
    allow_all_ext = ("--allow-all-ext" in __program_param)
    error_enable = ("--error-enable" in __program_param)
    etc_include = ("--etc-include" in __program_param)
    if not etc_include and "etc_include" in ls_pkg: etc_include = True
    repo = __get_dir(pkg)
    assert __is_dir(pkg), ValueError("target is not exist directory")
    with open(__join_path(repo, "MANIFAST.in"), "w") as fp:
        src = PyPInclude(pkg, allow_all_ext = allow_all_ext, error = error_enable)
        if "etc" in ls_pkg and __is_dir(__join_path(pkg, "etc") and etc_include: src += "\nrecursive-include etc/ *"
        fp.write(src)