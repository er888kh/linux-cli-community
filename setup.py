"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    r'(VERSION = "(\d.\d.\d)")',
    open("e_protonvpn_cli/constants.py").read(),
    re.M
).group(2)


long_descr = """
A fork of the official Linux CLI for ProtonVPN.

For further information and a usage guide, please view the project page:

https://github.com/ProtonVPN/linux-cli
"""


setup(
    name="e_protonvpn_cli",
    packages=["e_protonvpn_cli"],
    entry_points={
        "console_scripts": ["e_protonvpn = e_protonvpn_cli.cli:main"]
    },
    version=version,
    description="Linux command-line client for ProtonVPN",
    long_description=long_descr,
    author="Erfan Khadem",
    author_email="erfankhademerkh@gmail.com",
    license="GPLv3",
    url="https://github.com/er888kh/linux-cli-community",
    package_data={
        "e_protonvpn_cli": ["templates/*"]
    },
    install_requires=[
        "requests",
        "docopt",
        "pythondialog",
        "jinja2",
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
