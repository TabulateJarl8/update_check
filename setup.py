import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="updates",
    version="0.0.1",
    author="Tabulate",
    author_email="tabulatejarl8@gmail.com",
    description="Package to update the users copy of your file to the latest version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TabulateJarl8/updates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=[
		"requests",
		"tqdm"
	],
)
