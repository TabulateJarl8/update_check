[![PyPI version](https://badge.fury.io/py/update-check.svg)](https://badge.fury.io/py/update-check)
[![Downloads](https://pepy.tech/badge/update-check)](https://pepy.tech/project/update-check)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/TabulateJarl8/update_check/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/TabulateJarl8/update_check.svg)](https://GitHub.com/TabulateJarl8/update_check/issues/)


Update_Check is a Python module to implement in distributed programs. The functions as of now are checking for updates and updating a users Python file. It works by comparing the users Python file to the newest raw version of the file that's stored on a website like [GitHub](https://github.com).

# Usage
## Checking if File is Up to Date
----
One feature of this module is checking if the users file is up to date with the latest version. 
### Syntax:
pathToProgram(str): path to local file to be compared

programURL(str): URL to raw file on github (https://raw.githubusercontent.com/username/repo/file)
```python
isUpToDate(pathToProgram, programURL)
```
Heres an example of the ``isUpToDate()`` function:


```python
from update_check import isUpToDate

if isUpToDate(__file__, "https:///raw.githubusercontent.com/username/repo/myProgram.py") == False:
   doSomething()
```


This function will return True if the program is up to date with the web version and will return False if it's not. Note: ``__file__`` can be replaced with a path to a separate file.

&nbsp;

## Updating a File
----
To update a file using this module, you will need to use the ``update()`` function.
### Syntax:
```python
update(pathToProgram, programURL)
```

Here's an example of the ``update()`` function:


```python
from update_check import update

update(__file__, "https://raw.githubusercontent.com/username/repo/myProgram.py")
```


That block of code would grab the file from the URL and update the local file to that file. Note: ``__file__`` can be replaced with a path to a separate file.

&nbsp;

## Updating a File if it's not up to date
----
If you want a combination of the previous 2 functions, where it will check if a file isn't up to date, and if so, then it will update the file, then you want to use the ``checkForUpdates()`` function.
### Syntax:
```python
checkForUpdates(pathToProgram, URL)
```
Here's an example of the ``checkForUpdates()`` function:


```python
from update_check import checkForUpdates

checkForUpdates(__file__, "https://raw.githubusercontent.com/username/repo/myProgram.py")
```


The above block of code will test if the file specified, is not up to date, and if it isn't, it will update the file from the URL and return True. If it *is* up to date, then it will return False and do nothing. Note: ``__file__`` can be replaced with a path to a separate file.
