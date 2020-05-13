This utility  is used to create credits / attribution / license informaiton documentation of any software that uses open source code. 

The input to this utility is the Black Duck report (just the components.csv file).
Please generate a CSV report of your black duck project. Download the ZIP file. 
Unzip it and you will find the "componentXXXXXXX.csv" file. That will become input to this 
utility. 

The output is an HTML file which can be uploaded as the credits / attribution page. 


Prerequisites:  
You'll need docker installed in order to run this container .
See the Docker website(https://www.docker.com/get-started#h_installation) for installation instructions.

How to use this code?

1. Clone the repository: 
$ git clone https://github.com/studentchetan/attribution

2. Build the docker image
$ docker build -t attribution/app:1.0 .

3. Run the docker image, which will start everything up. The -p option forwards the container's port 5000 to port 3333 on the host.
$ docker run --name some-attribution -p 3333:5000 -d attribution/app:1.0

4. You can hit http://localhost:3333 in your browser to access the web interface of the tool. Upload "componentXXXXXXX.csv" file. Press 'Submit' button. You will be directed to 'upload' page, where generated attribution /credit HTML file is uploaded. You can click 'Download File' to download attribution / credit page. 


This tool has been inspired by chrome://credits/ page. 