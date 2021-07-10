# **Curseforge App API**
The package provides classes to interact Curseforge app API.

I wrote neither API nor documentation (btw documentation with methods and results took from [there]).

## Requirements 
```
requests>=2.25.1
selenium>=3.141.0
selenium-requests>=1.3
webdriver-manager>=3.4.2
```


## Examples:
```python
# getting API class
from curse_app_api import CurseAPI, WDCurseAPI

# creating API class
api = CurseAPI()

# example method 
print(api.get_category_timestamp())

# using with webdriver
wdapi = WDCurseAPI()

# example method 
print(wdapi.get_category_timestamp()) 
```


# Contributing
Feel free to contribute. So: 

1) If you find bugs related to this project, open an issue in 
Github issues tracker. 
2) If you want add a new feature, fork this repo, make changes locally and open a pull request. I'll check changes 
   myself and merge your code into main branch.


# TODO   
PyDocs for methods. As temp solution, you can use [this] link to see params and results.

[there]: https://curseforgeapi.docs.apiary.io/
[this]: https://curseforgeapi.docs.apiary.io/