Update_Check is a Python module to implement in distributed programs. The functions as of now are checking for updates and updating a users Python file. It works by comparing the users Python file to the newest version of the file that's stored on a website like [GitHub](https://github.com).

# Usage
## Checking if File is Up to Date
----
One feature of this module is checking if the users file is up to date with the latest version. 
### Syntax:
```python
isUpToDate(pathToProgram, programURL)
```
Heres an example of the ``isUpToDate()`` function:


```python
from update_check import isUpToDate

if isUpToDate(__file__, "https://github.com/username/repo/myProgram.py") == False:
   doSomething()
```


This function will return True if the program is up to date with the web version and will return False if it's not. Note: ``__file__`` can be replaced with a path to a file.

&nbsp;

## Updating a File
----
To update a file using this module, you will need to use the ``update()`` function.
### Syntax:
```python
update(programURL, pathToProgram)
```

Here's an example of the ``update()`` function:


```python
from update_check import update

update("https://github.com/username/repo/myProgram.py", __file__)
```


That block of code would grab the file from the URL and update the local file to that file. Note: ``__file__`` can be replaced with a path to a file.
