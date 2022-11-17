# *nopcommerce-framework*
## *Python Selenium Hybrid Framework* based on [SDET- QA Automation Techie youtube course](https://www.youtube.com/playlist?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf)
## [Store Demo - nopCommerce](https://www.nopcommerce.com/en/demo)

## Libraries
- selenium - browser automation library
- pytest - python testing framework
- pytest-html - html reports for pytest
- pytest-xdist - parallel tests execution
- openpyxl - excel files support for python
### *Libraries installation*
`pip install selenium pytest pytest-html pytest-xdist openpyxl`

## Folder Structure
- configurations/ - general data for all testcases(url, email, password)
- drivers/ - selenium webdrivers for chrome, edge and firefox browsers
- logs/ - python logging files
- pageobjects/ - classes representing application webpages
- reports/ - pytest html report
- screenshots/ - screenshots of failed testcases
- testcases/ - framework's all testcases and conftest.py
- testdata/ - excel file with emails and password for data driven tests
- utilities/ - classes and functions to work with excel sheets, *.ini files and python logging 
- run.bat

## Running Tests
### *run tests*
`pytest -v -s testcases/test_login.py`
### *run tests on desired browser*
```
pytest -v -s testcases/test_login.py --browser chrome
pytest -v -s testcases/test_login.py --browser edge
pytest -v -s testcases/test_login.py --browser firefox
```
### *run tests in parallel(n=num_of_threads)*
`pytest -v -s -n=2 testcases/test_login.py` 

## HTML Reports
### *Update conftest.py hooks*
### *run code*
`pytest -v -s -n=2 --html=reports/report.html testcases/test_login.py`