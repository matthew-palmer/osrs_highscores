import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osrs_highscores",
    version="0.1.3a0",
    author="Matthew Palmer",
    author_email="palmer.matthew167@gmail.com",
    description="Simple Wrapper for the OSRS Highscores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matt-palmer-tfs/osrs_highscores",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_reqires=[
        'requests==2.22.0',
    ]
)
