from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hello_world_alefcleto",
    version="0.0.1",
    author="alef_cleto",
    author_email="alefcleto@gmail.com",
    description="Print hello world",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alefcleto/hello_world_package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)