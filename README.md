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
