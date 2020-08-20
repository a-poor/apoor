import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="apoor",
    version="1.0.0",
    author="Austin Poor",
    author_email="a-poor@users.noreply.github.com",
    description="A small personal package written in Python with reusable code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/apoor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
    python_requires=">=3.6"
)
