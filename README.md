# Selenium Hybrid Framework

## NOPCOMMERCE

###	Prerequisite

1. Python 3 
1. Selenium: - Selenium libraries 
1. Pytest (6.0.1): - Python Unit Test Framework
1. pytest-html: - Pytest HTML reports
1. pytest-xdist (2.1.0): - Run tests parallel 
1. openpyxl: - MS Excel support

### What framework offers 
* Command line execution (No IDE required)
*	Custom configurations
*	Custom logger
*	Cross browser support
*	Parallel test execution
*	HTML reports 
*	Single test case or group of test cases can be run

### Folder structure
* Package: - Consist Python file
* Folder: - Images, log files, etc.

**Project Name** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PageObjects (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testCases (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br /> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Utilities (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TestData (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Configurations (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Logs (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Screenshots (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reports (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run.bat (File) <br />
<br />

### Folder Description 

* PageObjects: - Page object scripts. Script use to perform action on target site<br />

*	testCases: - Test cases<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              conftest.py: - fixtures<br />

*	Utilities: - Scripts for utilities like reading configuration file, logger configuration <br />

*	TestData: - Excel files, text files having test data<br />

*	Configurations: - Configuration file<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                   config.ini: - driver locations, log file location etc.<br />

*	Logs: - Log file of run<br />

*	Screenshots: - HTML page screenshots (mostly  ’.png’ format) to understand pop-up, Arbitrary failures<br />

*	Reports: - HTML reports of run<br />


### Getting Started

*	Clone the repository
 &nbsp;&nbsp;	`git clone https://github.com/BatataWada1/NOP-commerce.git`
*	Go to Configuration folder and edit the config.ini file
* Go to nopcommerce\testCases and execute command

### Commands to run

*	To Run the single test case <br />
 &nbsp;&nbsp;&nbsp;`pytest -v -s test_login.py`<br />

* To Run on specific browser &nbsp;&nbsp; **(Mozilla Firefox is default)**<br />
&nbsp;&nbsp;&nbsp;`pytest -v -s test_login.py –-browser chrome`  

* For parallel execution  &nbsp;&nbsp **(-n <num> runs the tests by using multiple workers)** <br />
 &nbsp;&nbsp;&nbsp;`pytest -v -s -n 3 test_login.py` 				
 
* To generate HTML report<br />
`pytest -v -s -n 2 --html ..\Reports\report.html test_login.py --browser chrome`

