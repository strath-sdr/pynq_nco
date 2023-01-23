import os
from distutils.dir_util import copy_tree
from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
repo_board_folder = f'boards/{board}'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'pynq_nco'

data_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(repo_board_folder):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError(
            "Directory {} does not exist.".format(board_notebooks_dir))

# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(repo_board_folder, package_name, 'bitstream')
    dst_ol_dir = os.path.join(package_name, 'bitstream')
    copy_tree(src_ol_dir, dst_ol_dir)
    data_files.extend(
        [os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

check_env()
copy_overlays()

setup(
    name=package_name,
    version='1.0.1',
    install_requires=[
        'pynq==2.7',
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="PYNQ NCO Example @ StrathSDR.")
