This utility ( license.py ) is used to create credits / attribution / license informaiton documentation of any software that uses open source code. 

The input to this utility is the Black Duck report (just the components.csv file).
Please generate a CSV report of your black duck project. Download the ZIP file. 
Unzip it and you will find the "componentXXXXXXX.csv" file. That will become input to this 
utility. 

The output is an HTML file which can be uploaded as the credits / attribution page. 


Requirements: 
 
python3, pandas

create a virutual environment 
$python3 -m venv attribution 

Activate the virutal env 
$ source attribution/bin/activate 

$ cd attribution 

Install Pandas
$pip install pandas

Clone the repository: 
$git clone https://github.com/studentchetan/attribution

$cd attribution     <<< The source code license.py and lic text files are here >>> 

Then run, 
python3 license.py -p <prodname> -i <inputfile> -o <outputfile>

For example: 
python3 license.py -p "Cloud Reporting Service" -i components-cr-20200416.csv -o credits.html

the output will be found in the same folder : credits.html 

When no argument is provided to the command line, then: 

Product Name = "Myproduct" 
inputfile  = "components.csv"
outputfile = "credits.html"


This tool has been inspired by chrome://credits/ page. 

