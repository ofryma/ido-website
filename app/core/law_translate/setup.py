from setuptools import setup, find_packages

def read_requirements():
    """Reads dependencies from requirements.txt"""
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="law-translate",
    version="0.1.0",
    author="Ofry Makdasy",
    author_email="ofry60000@gmail.com",
    description="A package for translating legal documents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)