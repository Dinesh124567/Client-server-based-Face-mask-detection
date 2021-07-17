# Client-server-based-Face-mask-detection

## Project requirements

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

In order to run the project we require 
 
* hardware - 
  * LAN network connection, wifi module to connect LAN network where the [RESTAPI](https://www.redhat.com/en/topics/api/what-is-a-rest-api) is hosted
  * to host REST api or run host script , a host system with atleast 8 gb of ram with i5 processor and running on windows operating system is required
  * client systems which is connected to [camera access](https://www.hunker.com/13419198/how-to-connect-a-cctv-camera-to-a-computer)
            

* software - 
  * [python 3.6](https://www.python.org/downloads/release/python-360/)
	  

## Project Execution

This project consists of two things,
    
* 1) Host script - a python main script which is suppossed run on host machine , it will host REST api and initiate [SWAGGER UI](https://swagger.io/tools/swagger-ui/) for access to face-mask detection api via browser

* 2) server script - a simple python script which is supposed to run on client machine where the face-mask detection needed runtime request send - it is used for dynamic live face mask detection

### Procedure for execution

*  first select a host machine by considering good specifications since the deep learning pretrained models are going to load and execute on this machine. now install all the required packages in system using command
    
    ` pip install -r requirements.txt `

*  make sure the host machine is connected to LAN network where all the client systems are also connected to the same network
   
*  now run the host main script which initiates REST api host
       
       ` python fastApi.py `

*  copy the local ip address of the host machine - (example 192.168.1.40), this ip address with port number combined is used to access the project [SWAGGER UI](https://swagger.io/tools/swagger-ui/) where you can see one method, you can upload the image / video footage as request to api and the host machine recieves request and processes for face-mask detection, sends back the output.

*  to run live facemask detection, copy the client script to any of the client machine and execute the client side script with following command
   
   ` python client.py http://{host local ip address}:8000/facemask_detect `

