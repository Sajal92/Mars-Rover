# Problem - Mars Rover

## Instructions to Run

* Open terminal inside the folder containing the source code i.e app folder
* To run the unit tests just type the command ``` pytest ``` and press ```enter```
* To get the flask api up and running use following commands:
```
docker image build -t rover .
docker run -p 5000:5000 -d rover
```
* Go to your browser and enter the url: <b>localhost:5000</b>
* There you can enter input configuration for the rovers and press submit to generate the output.<br /> If the entries are wrong the output will contain error messages, otherwise the final states of all the rovers.

## Brief Introduction
Code has been developed using TDD approach in a OOP layout and supplied as a python package. 
A brief explanation of the code:
* ```navigate.py``` contains the MarsRover class which provides the functionalities to navigate the rover on plateau
* ```app.py``` conatins the flask api wrapper for the MarsRover class
* ```test_navigate.py``` contains various unit-tests eg. hard coded test cases, tests for missing entries, rover lost and clash test cases, invalid entries cases etc.
* API runs in a docker container with configuration provided in Docerfile
  
#### Assumptions:
* Rovers are landed and navigated on the plateau sequentially
* The lower-left coordinates of plateau are assumed to be 0,0.
* No limit for the number of rovers
