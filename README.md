# pythonGlobDemo

Python 3.9 and the glob module

This is a repo of code vomit from looking at and using the python glob module. 

This code was written to test module methods for POC and is not production code (yet).

Based on reading this site
https://docs.python.org/3.9/library/glob.html#module-glob

Walk Through steps
- clone this repo

  `git clone https://github.com/jk8260/pythonGlobDemo.git`
- run [findRegEx](https://github.com/jk8260/pythonGlobDemo/blob/master/findRegEx.py)
  
  `python3 findRegEx.py`

  ![image](https://user-images.githubusercontent.com/10749423/209390544-fa9c1486-73cf-4c13-ad06-ac0800cd161f.png)

- run [searchInsideJson](https://github.com/jk8260/pythonGlobDemo/blob/master/searchInsideJson.py)
  
  this takes 1 arg which is what to search for in the files. 
  
  If nothing is passed I wired it to search for 'event' which is in all example files
  
  `python3 searchInsideJson.py` 
  
  ![image](https://user-images.githubusercontent.com/10749423/209388291-32ed7c2f-b354-46f1-925d-650b359ca5f9.png)

  
  `python3 searchInsideJson.py [searchword]`

  `python3 searchInsideJson.py Lester`
  
  ![image](https://user-images.githubusercontent.com/10749423/209390064-3691c162-8563-4be1-96a2-71c20cf0e637.png)


This example has two data sub folders, to test the recursive flag (recursive does not seem to work yet for me)

There are also .txt files to be sure they are excluded.

![image](https://user-images.githubusercontent.com/10749423/209388621-c275c4f6-c70b-4a9d-8311-a24f490367e3.png)

