This utility ( license.py ) is used to create credits / attribution / license informaiton documentation of any software that uses open source code. 

The input to this utility is the Black Duck report (just the components.csv file).
The output is an HTML file which can be uploaded as the credits / attribution page. 


Requirements: 

Use 
python3 virtual environment 
pip install pandas << install Pandas 

clone the code.  

Then run, 
python3 license.py -p <prodname> -i <inputfile> -o <outputfile>

This tool has been inspired by chrome://credits/ page. 

