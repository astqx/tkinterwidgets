import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkinterwidgets",
    version="0.0.2",
    author="Aditya Singh Tejas",
    author_email="adityasinghtejas03@gmail.com",
    description="Tkinter Custom Widgets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AST07/tkinterwidgets",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.0',
)