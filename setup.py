"""Setup script for idealista7"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="idealista7",
    version="1.0.0",
    author="BACH Studio",
    author_email="contact@bachstudio.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BACH-AI-Tools/idealista7",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # 添加你的依赖
    ],
)
