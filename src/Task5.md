### Question 5

Have a browse of [FastAPI](https://github.com/tiangolo/fastapi) and write down how this repository is structured and why. What improvements do you think can be made?

#### FastAPI
The FastAPI repo is broken down into 6 main folders:
1. docs
    This contains the documentation of FastAPI. There are also multiple languages available for the documentation.
2. docs_src
    This folder provides tutorials on the different use cases of FastAPI.
3. fastapi
    This folder contains the source code for fastapi itself. 
4. scripts
    This folder contains the different scripts needed to perform various tasks in the development of FastAPI.
5. tests
    This folder contains the test cases for FastAPI
6. .github
    This folder is for github related files, including workflows and actions 

### Improvements
The naming convention of the folders could be better, for example, docs_src does not immediately make the user think that they should visit the folder for tutorials and examples. Using fastapi as the folder name is also not conventional, as most people would expect a src folder instead

Certain naming conventions of the file are also not the best. For example, [here](https://github.com/tiangolo/fastapi/blob/d666ccb62216e45ca78643b52c235ba0d2c53986/tests/test_modules_same_name_body/app) we can see that there are 2 files, [a.py](https://github.com/tiangolo/fastapi/blob/d666ccb62216e45ca78643b52c235ba0d2c53986/tests/test_modules_same_name_body/app/a.py) and [b.py](https://github.com/tiangolo/fastapi/blob/d666ccb62216e45ca78643b52c235ba0d2c53986/tests/test_modules_same_name_body/app/b.py) whose names are not informative enough on what they might contain. 

Lastly, some of the documentation for other languages do not work, for example, [here](https://github.com/tiangolo/fastapi/blob/d666ccb62216e45ca78643b52c235ba0d2c53986/docs/id/docs/index.md). We can see that the documentation is still in English. 

Overall, it is a decently well structured repository, given the number of people who work on it. It is user friendly enough that people should be able to use and understand it with a little bit of exprimentation. 