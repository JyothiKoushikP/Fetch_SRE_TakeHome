# Fetch Take Home Exercise - Site Reliability Engineering

### Problem Statement

Implement a program to check the health of a set of HTTP endpoints. A basic overview is given
in this section. Additional details are provided in the Prompt section.

Read an input argument to a file path with a list of HTTP endpoints in YAML format. Test the
health of the endpoints every 15 seconds. Keep track of the availability percentage of the HTTP
domain names being monitored by the program. Log the cumulative availability percentage for
each domain to the console after the completion of each 15-second test cycle.

Each HTTP endpoint element in the YAML list has the following schema:

● name (string, required) — A free-text name to describe the HTTP endpoint.

● url (string, required) — The URL of the HTTP endpoint.
- You may assume that the URL is always a valid HTTP or HTTPS address.

● method (string, optional) — The HTTP method of the endpoint.
- If this field is present, you may assume it’s a valid HTTP method (e.g. GET, POST,
etc.).
- If this field is omitted, the default is GET.

● headers (dictionary, optional) — The HTTP headers to include in the request.
- If this field is present, you may assume that the keys and values of this dictionary
are strings that are valid HTTP header names and values.
- If this field is omitted, no headers need to be added to or modified in the HTTP
request.

● body (string, optional) — The HTTP body to include in the request.
- If this field is present, you should assume it's a valid JSON-encoded string. You
do not need to account for non-JSON request bodies.
- If this field is omitted, no body is sent in the request.

Running the health checks
After parsing the YAML input configuration file, the program should send an HTTP request to
each endpoint every 15 seconds. Each time an HTTP request is executed by the program,
determine if the outcome is UP or DOWN:

● UP — The HTTP response code is 2xx (any 200–299 response code) and the response
latency is less than 500 ms.

● DOWN — The endpoint is not UP.

Logging the results
Each time the program finishes testing all the endpoints in the configuration file, log the
availability percentage of each URL domain over the lifetime of the program to the console.
Availability percentage is defined as:
100 * (number of HTTP requests that had an outcome of UP / number of
HTTP requests)

User presses CTRL+C and the program exits.
Note that when logging the availability percentage for each domain, the program should round
floating-point availability percentages to the nearest whole percentage.

### Technologies Used

● Operating System: MacOS 14.6.1  
● Python (Version: 3.6) {Project Code}  
● Docker (Version 27.3.1) {Building the Image and Running Containers}  
● YAML (Yet-Another Markup Language) {Input Parsing}  
● GitHub {Version-Control, Storing Code Repositories}


### Project Structure

project/  
│  
├── Dockerfile  
├── requirements.txt  
├── main.py  
├── Input.yml  
├── Logger.py  
├── ParseYamlInput.py  
├── HttpRequest.py  
├── HttpChecker.py  
├── AvailabilityTracker.py  
└── README.md  

### Files Description

● Input.yaml  
The Default YAML configuration file consisting of the HttpRequests (URL, Method, headers and body) and other parameters.
This input is used to process the HttpRequests and calculate the availability percentage.
This file can be modified on execution time which is discussed below.

● HttpRequest.py  
This module defines a class "HttpRequest" that represents an HTTP Request. It encapsulates all the necessary 
attributes like name, URL, method, headers and body and provides a detailed structure.
The class also contains setter and getter methods to promote validation and security.

● ParseYamlInput.py  
This module is responsible for reading the Input.yml file, parsing it and converts it into Python Objects. 
It reads the HTTP Request Configurations and transforms them into HttpRequest Objects used for making the request 
and calculating the availability.

● HttpChecker.py  
This module is responsible for sending the actual Http Requests. It uses the HttpRequest objects 
created by the ParseYamlInput and performs the request, returning the status of each service.  
- Key Functions:  
-- send_request(http_request): Sends an HTTP request based on the given HttpRequest object and 
returns the response or error message.  
-- check_availability(response): Evaluates the response to determine the service's availability.

● AvailabilityTracker.py  
This module is responsible to keep track of the availability status of various services. It stores and logs
whether the services are available or not, and it can provide summaries, such as uptime or downtime statistics.
- Key Functions:  
  -- track_availability(http_request, status): Records the availability status of a specific request.  
  -- generate_report(): Outputs a summary report of the availability status for all services.

● Logger.py  
This module is responsible for logging important events during the execution of the program. It can be used to track the status of Http Requests,
any exceptions and the final results of availability checks. It helps in debugging and monitoring the program's performance.

● main.py  
The main entry point for the project. It orchestrates the entire process, including reading input configurations from Input.yml, 
initializing logging and using other modules like HttpRequest, HttpChecker, AvailabilityTracker and ParseYamlInput to perform all required tasks.

● README.md  
The README file provides documentation for the project. It explains how to set up and run the application, 
as well as providing an overview of what each file/part of the project does.

● Requirements.txt  
The file consists of all the python dependencies required to run the project. This file is automatically taken when 
building the Docker image or setting up the project locally. "pip" is the package manager used to install the dependencies.

● Dockerfile  
The Dockerfile contains instructions for building a Docker image for this project. It defines 
the base Python image, dependencies, copy the necessary files and runs the main.py file.
For the project, running this file would be enough to execute the project. All the dependencies, modules are tested and will be handled by the Docker Image.

### Running the Project Code

The main reason of bringing the concept of Containers in this project is to provide ease of usability to the user.
Different users use different environments, operating systems, configurations and it is extremely difficult to setup all the
dependencies and project code.

With only one tool, this code can be wrapped with all the dependencies, packages and can be executed from any system
irrespective of diverse conditions. We are using Docker for this use-case which is free, easy to use and efficient.

● Image  
A Docker image is a lightweight, standalone, and executable package that contains 
everything needed to run a piece of software, including the application code, libraries, 
environment variables, dependencies, and configurations.

● Container  
A Docker container is a runtime instance of a Docker image. It encapsulates an application and its 
dependencies in an isolated environment. 
Containers are portable, scalable, and lightweight.

● Docker  
Docker is an open-source platform that automates the deployment, scaling, 
and management of applications using containerization. It provides public/private images which you can use to build your own image. 
It provides OS-Level Virtualization.

**INSTALLING DOCKER**  
Installing and Using Docker is very simple:
The Below link has all the pre-defined instructions to install Docker on various Operating system Configurations.

https://docs.docker.com/engine/install/

This will ensure you have Docker Desktop and Docker CLI Installed.

**DOWNLOADING THE PROJECT CODE**  
Now you have the Docker Desktop / CLI Setup, the next step would be downloading the project code
There are 2 ways to do it. 

● Using GitHub / Git  
If you have the knowledge of using GitHub / Git, you can clone the repository to your local system and run the project at your comfort and ease.

● Public Code URL   
I have also included a publicly-accessible URL that contains the project code that you can just download, extract and use it in your local system.

After installing Docker and Downloading the source code on your local system and extracting it.
The Folder should look something like this:

<Image

**BUILDING THE DOCKER IMAGE**  
Open your terminal/ PowerShell / Git Bash console and navigate to the project code directory in your system
(Use cd linux command ). This Step is extremely crucial.

The first step is to build the docker image (I have also included the tar file of the docker image in case you want to use it)

> docker build -t <Image_Name_Your_Choice> .

You can check the images you have built using the following command:

> docker images

The console output would be similar to this:

![](/Users/jyothikoushikpaladugu/Desktop/scr1.png)

**RUNNING THE DOCKER CONTAINER**  
Now, the only step remaining is to run the docker container using the image you have just built. I offer a lot of flexibility.
As discussed in the problem statement, the code requires a YAML file to parse and process the requests.

By Default the image has a Input.yml file (The mock input provided in the assignment document)
You can run that. This can be done using the following command:

> docker run -it <IMAGE_NAME>

**Remember: The Test Cycle runs infinitely every 15 seconds, in order to step please press Ctrl + C**

If you have your input and would like to test that, you can do it very easily using the following command:

> docker run -it -v <Input_File_Absolute_Path>:/app/Input.yml <IMAGE_NAME>

This will volume mount your input to the container and you can run the program using any custom input and the code will process it automatically.

**Note: All the execution process has been recorded in a demonstration video that I have attached with this repository, If you have any difficulties, please watch that video and it will be helpful.**

### Sample Output

After running the docker container,your output will be similar to the sample output shown below:

![](/Users/jyothikoushikpaladugu/Desktop/scr2.png)

### Project Code Properties

● Re-usability  
The project code builds a docker Image which is customizable. The Image could be run any number of times promoting easiness, re-usability.

● Security  
The code promotes security in many ways:
- Private Attributes: The main HttpRequest class is private which means no other module can access it directly and can access it using only getter / setter functions.
- No Hardcoded Credentials: There is no hard coding of input, credentials and other sensitive data. Everything is handled dynamically using environment variables.
- Modularity: Modularity of the code and Single Responsibility Principle ensures that no modules clash with each other functionalities.

● Portability  
The Docker Image you have built could be shared to other people easily using the tar file format which promotes portability.

● Error Handling
All case scenarios have been analyzed and exceptions are handled to make sure that the code doesn't break on execution.
(Ex: Invalid Input (No Name/URL), Invalid File Input, Invalid Requests etc.)

### Assumptions Taken for the Assignment:

● I have assumed that whoever runs this code has minimal knowledge of the programming language I have used.   
Docker Containers is the primary approach used so that anyone can just install Docker, 
download the code and run it by building the image.

● I have assumed that none of the requests are dependent on other preceding requests and all are completely independent. 










