import os
import setuptools

here = str(os.path.abspath(os.path.dirname(__file__)))

with open("README.md", "r") as f_readme:
    long_description = f_readme.read()

about = {}
with open(os.path.join(here, 'osrs_highscores', '__version__.py'), 'r') as f_version:
    exec(f_version.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about['__url__'],
    license=about['__license__'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=[
        'requests==2.27.1',
        'beautifulsoup4==4.11.1',
        'addict==2.4.0'
    ]
)
