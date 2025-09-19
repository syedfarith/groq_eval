from setuptools import setup, find_packages
import pathlib

this_dir = pathlib.Path(__file__).parent
long_description = (this_dir / "README.md").read_text()
setup(
    name="groq-eval-score",  # must be unique on PyPI
    version="0.2.0",
    description="A package to evaluate output relevancy using Groq LLM",
    long_description=long_description,
    long_description_content_type="text/markdown",  # <-- important!
    author="Syed Farith C",
    author_email="syedfarith1351@gmail.com",
    packages=find_packages(),
    install_requires=["groq"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
