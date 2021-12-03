import setuptools
from setuptools import find_packages

setuptools.setup(
    name="zendesk",
    version="0.1.15",
    author="Anamitra Musib (ana1998musib@gmail.com)",
    description="A CLI to interact with the Zendesk Tickets API",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "requests >= 2.26.0",
        "tabulate >= 0.8.9",
    ],
    entry_points={"console_scripts": ["zendesk=zendesk.__main__:main"]},
    py_modules=["zendesk", "zendesk.src", "zendesk.utils"],
    python_requires=">=3.5",
)
