import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setuptools.setup(
    name="pyng",
    version="0.1.0r",
    author="Renaud Gaspard",
    author_email="gaspardrenaud@hotmail.com",
    description="Command utility to ping multiple hosts at once",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Renaud11232/pyng",
    packages=setuptools.find_packages(),
    entry_points=dict(
        console_scripts=[
            "pyng=pyng.command_line:main"
        ]
    ),
    install_requires=[
        "ping3"
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
