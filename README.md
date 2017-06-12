# BLUE / GREEN and A / B OpenShift Demo

This repository provides a sample Python web application implemented using the Flask web framework and hosted using ``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Deployment Overview
There are two ways that you can conduct this demo, via the ``oc`` tool or using the web console. In the next section I will layout the steps of a typical OpenShift Ops discussion.

#### Steps:
1. Deploy the _blueflask_ application.
2. Expose _blueflask_ to the outside world using a route.
2. Test the application using ``apicall.py``.
3. Scale the _blueflask_ application.
4. Show how OpenShift loadbalances the _blueflask_ app.
5. Deploy the _greenflask_ application.
6. Edit the _blueflask_ route to use the _greenflask_ service.
7. Test the traffic and show we had a hard cut over from _blueflask_ to _greenflask_.
7. Discuss _Blue/Green_ cut over could work.
8. Change the route back to _blueflask_ and create a new route for _greenflask_.
2. Create a new route called _AB_ and split the traffic 90/10 between _blueflask_ and _greenflask_.
1. Run a test showing that the trafic is being split between both _blueflask_ containers and _greenflask_ containers.


## Deployment Steps (Web Console)

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, ``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

Link to PDF coming...

The HTTPS URL of this code repositories which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/mwardRH/blueflask.git
* https://github.com/mwardRH/greenflask.git



## Deployment Steps (``oc``)
Using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, run the following:

## Blue / Green Deployment

#### Sign into the web server:
```
oc login -u admin
```
#### Create a new Project:
```
oc new-project flask --display-name='Flask Project' --description='Blue Green Deployment Demo'
```

#### Deploy the _blueflask_ python web application:   
```
oc new-app https://github.com/mwardRH/blueflask.git
```
#### Create an external route for _blueflask_:
```
oc expose service blueflask
```
#### Run apicall.py library.
Enter the hostname for the route exposed in your environment. If you run into an error first try to browse to the site and validate it's working. If you see the web application working go to the apicall.py section of this document for more help.
```
python apicall.api ip-address-of-route
```

#### Scale your application:
Scale the application to show how easy it is to add capacity, and to show the automatic load balancing of OpenShift. After the application is scaled run the ``apicall.py`` app again. Notice the hostname is alternating on a 50/50 split.
```
oc scale deploymentconfig --replicas=2 blueflask
```

#### Deploy version 2 of the application called _greenflask_:
```
oc new-app https://github.com/mwardRH/greenflask.git
```

#### Cut over routed traffic to new version 2 _greenflask_:
We are going to cut the traffic over from _blueflask_ to _greenflask_. This is meant to represent Blue to Green application deployment model. This assumes v2 _greenflask_ will go online taking over the main URL from _blueflask_. There is no transition and it assuems _greenflask_ has passed all testing requirements. After running the command below use the ``callapi.py`` script to show the cutover was clean.

```
oc patch route/blueflask -p '{"spec":{"to":{"name":"greenflask"}}}'
```

#### Move the route back to _blueflask_:
We are going to move the route back to the _blueflask_ application. This could represent yet another version of the web application or it could represent a failure and an emergency abort of the new application. We are going to rever it back to show a different and better deployment method called A-B Deployment. Remember to run the ``apicall.py`` script to show the cut back was successful.
```
oc patch route/blueflask -p '{"spec":{"to":{"name":"blueflask"}}}'
```

## A / B Deployment

#### Create a route for _greenflask_:
```
oc expose service greenflask
```

#### Test _greenflask_ route:
Validate the route for _greenflask_ works properly by using the ``apicall.py`` application and putting in the hostname for _greenflask_.
```
python apicall.api ip-address-of-route
```

#### Create a new route called ab-deploy





## ``apicall.py`` Section
``apicall.py`` is a python application, written by Matthew Ward, that reaches out to a web server and prints the content of web page. It's a fairly simple application that takes 1 arugment from stdin for the URL. ``apicall.py`` uses a popular python package called _request_ to fetch the contents of the URL. _request_ is a non-standard python package so you may need to install it.

### Getting Started
#### Download _flaskdemo_ from github:
```
https://github.com/mwardRH/demoflask.git
```
#### Install _request_ package:
There are multiple ways to install the requests package. I am only going to outline the _python_ way and the _Fedora_ way.

###### Python Way:
```
pip install -r requirements.txt
```

###### Fedora Way:
```
dnf install python3-requests
```
