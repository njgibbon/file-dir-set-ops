from setuptools import setup
from setuptools import find_packages

setup(
    name='file-dir-set-ops',
    description='Set Operations on File Directories.',
    long_description='Set Operations on File Directories.',
    url='https://github.com/njgibbon/file-dir-set-ops',
    version='0.0.0.3',
    author="Nick Gibbon",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'file-dir-set-ops = file_dir_set_ops.main:main',
        ],
    }
)
