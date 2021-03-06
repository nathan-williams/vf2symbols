# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Just a toy, enough setuptools to be able to install.
"""
from setuptools import setup, find_packages

setup(
    name="vf2symbols",
    use_scm_version={"write_to": "src/vf2symbols/_version.py"},
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'vf2symbols=vf2symbols.vf2symbols:main',
        ],
    },

    setup_requires=["setuptools_scm"],
    install_requires=[
        "absl-py>=0.9.0",
        "fonttools[ufo]>=4.13.0",
        "lxml>=4.0",
        "nanoemoji>=0.2.0",
        "ninja>=1.10.0.post1",
    ],
    python_requires=">=3.6",

    # this is for type checker to use our inline type hints:
    # https://www.python.org/dev/peps/pep-0561/#id18
    package_data={"vf2symbols": ["py.typed"]},

    # metadata to display on PyPI
    author="Rod S",
    author_email="rsheeter@google.com",
    description=(
        "Exploratory utility to convert variable icon fonts into "
        "custom symbols for use on Apple platforms "
        "(https://developer.apple.com/documentation/xcode/creating_custom_symbol_images_for_your_app)"
    ),
)