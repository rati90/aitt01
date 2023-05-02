import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aitt01", # Replace with your username
    version="1.0.0",
    author="Rati Bakhtadze",
    author_email="ratibakhtadze@gmail.com",
    description="Test python whl package for training purposes Lab Course 02.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rati90/aitt01",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    options = {"bdist_wheel": {"universal":True}},
    python_requires='>=3.7',
)