import pandas as pd
import os
import sys, getopt

htmlhead = '''
<!-- Generated by licenses.py; do not edit. -->
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<meta name="color-scheme" content="light dark">
<title> Credits </title>
'''


style = '''
<style>
    html {
      --sophos-blue-50: rgb(229, 230, 241);
      --sophos-blue-300: rgb(108, 161, 247);
      --sophos-blue-600: rgb(46, 112, 199);
      --sophos-blue-900: rgb(23, 78, 166);
      --sophos-grey-200: rgb(232, 234, 237);
      --sophos-grey-800: rgb(60, 64, 67);
      --sophos-grey-900: rgb(32, 33, 36);
    
      --interactive-color: var(--sophos-blue-600);
      --primary-color: var(--sophos-grey-900);
    
      --product-background: var(--sophos-blue-50);
      --product-text-color: var(--sophos-blue-900);
    
      background: white;
    }
    
    @media (prefers-color-scheme: dark) {
      html {
        --interactive-color: var(--sophos-blue-300);
        --primary-color: var(--sophos-grey-200);
    
        --product-background: var(--sophos-grey-800);
        --product-text-color: var(--sophos-grey-200);
    
        background: var(--sophos-grey-900);
      }
    }
    
    body {
      color: var(--primary-color);
      font-size: 84%;
      max-width: 1020px;
    }
    a {
      color: var(--interactive-color);
    }
    .page-title {
      font-size: 164%;
      font-weight: bold;
    }
    .product {
      background-color: var(--product-background);
      color: var(--product-text-color);
      border-radius: 5px;
      margin-top: 16px;
      overflow: auto;
      padding: 2px;
    }
    .product .title {
      float: left;
      font-size: 110%;
      font-weight: bold;
      margin: 3px;
    }
    .product .homepage {
      color: var(--interactive-color);
      float: right;
      margin: 3px;
      text-align: right;
    }
    .product .homepage::before {
      content: " - ";
    }
    .product .show {
      color: var(--interactive-color);
      float: right;
      margin: 3px;
      text-align: right;
      text-decoration: underline;
    }
    .licence {
      border-radius: 3px;
      clear: both;
      display: none;
      padding: 16px;
    }
    .licence h3 {
      margin-top: 0;
    }
    .licence pre {
      white-space: pre-wrap;
    }
    .dialog #print-link,
    .dialog .homepage {
      display: none;
    }
    input + label + div {
      display: none;
    }
    input + label::after {
      content: "show license";
      cursor: pointer;
    }
    input:checked + label + div {
      display: block;
    }
    input:checked + label::after {
      content: "hide license";
      cursor: pointer;
    }
    </style>
    '''

closehead = f"</head>"
openbody = f"<body>"

def maplictext(licnames):
    files = []
    if ('GNU General Public License v1.0' in licnames ):
        files.append('gplv1.0.txt')
    if ('GNU General Public License v2.0' in licnames ):
        files.append('gplv2.0.txt')
    if ('GNU General Public License v3.0' in licnames ):
        files.append('gplv3.0.txt')
    if ('GNU Lesser General Public License v2.1' in licnames ):
        files.append('lgplv3.0.txt')
    if ('GNU Lesser General Public License v3.0' in licnames ):
        files.append('lgplv3.0.txt')
    if ('BSD 3-clause' in licnames):
        files.append('BSD-3-clause.txt')
    if ('Apache License 2.0' in licnames):
        files.append('apache2.0.txt')
    if ('MIT License' in licnames):
        files.append('mit.txt')
    if ('Eclipse Public License 1.0' in licnames):
        files.append('eplv1.0.txt')
    if ('Eclipse Public License 2.0' in licnames):
        files.append('eplv2.0.txt')
    if ('Common Development and Distribution License 1.1' in licnames):
        files.append('cddlv1.0.txt')
    if ('Common Development and Distribution License 2' in licnames):
        files.append('cddlv2.0.txt')
    if ('Mozilla' in licnames):
        files.append('mplv2.0.txt')
    
    print (files)
    lictext = ""
    for f in files: 
        with open (f, 'r') as fd:
            lictext = lictext + fd.read()
    
    return lictext

    



#Build one lic 

def buildlicrow (component, index, lictext):
    row = ""

    hdr = f'''
    <div style="clear:both; overflow:auto;">
    <div class="product">
    <span class="title">{component}</span>
    <!-- TBD: Add in when ready for the homepage 
    <span class="homepage"><a href="https://github.com">homepage</a></span>
    -->
    <input type="checkbox" hidden id="{index}">
    <label class="show" for="{index}" tabindex="{index}"></label>
    <div class="licence">
    <pre>
    '''
    #with open(filename, 'r') as f:
    #   lictxt = f.read()

    tail = '''
    </pre>
    </div>
    </div>
    '''
    row = hdr + lictext + tail
    return row
 
close = "</div></body> </html>"

def outhtml(inputfile, outputfile, productname):
    if os.path.isfile(inputfile):
        nds = pd.read_csv(inputfile, usecols=[3,7])
    else:
        print ("Input file does not exist")
        sys.exit(2)

    if os.path.isfile(outputfile):
        os.remove (outputfile)
        

    with open(outputfile, 'a') as f:
        #file openers
        f.write (htmlhead)
        f.write (style)
        f.write (closehead)
        f.write (openbody)
        h2 = f"<h2> Credits - {productname} </h2>"
        f.write (h2)

        for ind in nds.index:
            row = buildlicrow (nds['Component name'][ind], ind, maplictext(nds['License names'][ind]))
            f.write (row)
        
        f.write (close)

def main(argv):
   inputfile = 'components.csv'
   outputfile = 'credits.html'
   productname = 'Myproduct'
   try:
      opts, args = getopt.getopt(argv,"h:i:p:o:",["ifile=","ofile="]) 
   except getopt.GetoptError:
      print ('license.py -i <inputfile> -o <outputfile> -p <product name>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('license.py -p <prodname> -i <inputfile> -o <outputfile> -p <product name>')
         sys.exit()
      elif opt in ("-p", "--product"):
          productname = arg
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   outhtml(inputfile, outputfile, productname)

if __name__ == "__main__":
   main(sys.argv[1:])
