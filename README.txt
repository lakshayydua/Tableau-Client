This package contains sample code written in Python to demonstrate various ways to use the Tableau Server REST API.

Required tools:
    1. Tableau Server 10.0. This sample is hard-coded to make requests using version 2.3 of the REST API, which requires Tableau Server 10.0.
    2. Python 2.7 or 3.3+

Optional tools:
    1. Pip Package Manager (https://pip.pypa.io/en/latest/installing.html)

Required Python libraries:
    1. requests v2.5.3
        a. License : http://docs.python-requests.org/en/latest/user/intro/#apache2
        b. Download: http://docs.python-requests.org/en/latest/user/install/#install

Getting started:
    1. Install the tools listed in the "Required tools" section.
    2. Download all libraries listed in the "Required Python libraries" per the installation instructions for the libraries. We recommended using the pip package manager (e.g. "pip install requests")
    3. Open the "REST-API-sample-2_3.py" file using a text editor.
    4. Navigate to the section labeled "Global Variables -- CONFIGURE THESE BEFORE RUNNING" in the __main__ function.
    5. Set the variables (server, username, password, and optionally workbook).

Running the sample:
    1. Make sure that Tableau Server version 10.0 is running. 
    2. Open a command prompt (e.g. "cmd" in Windows).
    3. In the command prompt window, change to the folder where you have the sample code.
    4. Enter "python REST-API-sample-2_3.py"

