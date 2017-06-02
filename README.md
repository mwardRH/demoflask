# BLUE / GREEN OpenShift Demo

This repository provides a sample Python web application implemented using the Flask web framework and hosted using ``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Deployment Overview
There are two ways that you can conduct this demo, via the ``oc`` tool or using the web console. In the next section I will layout the steps of a typical OpenShift Ops discussion.

#### Steps:
1. Deploy the _blueflask_ application.
2. Expose _blueflask_ to the outside world using a route.
2. Test the application using ``apiCall.py``.
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

The HTTPS URL of this code repositories which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/mwardRH/blueflask.git
* https://github.com/mwardRH/greenflask.git

## Deployment Steps (``oc``)


If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://github.com/mwardRH/blueflask.git
```

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://github.com/mwardRH/blueflask.git
```
