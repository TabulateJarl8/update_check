import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="update_check",
    version="0.0.11",
    author="Tabulate",
    author_email="tabulatejarl8@gmail.com",
    description="Package to update the end-users copy of your file to the latest version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TabulateJarl8/update_check",
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
