# Flask Application V1 (BLUE Release)

This repository provides a sample Python web application implemented using the Flask web framework and hosted using ``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Deployment Steps

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, ``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/mwardRH/blueflask.git

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://github.com/mwardRH/blueflask.git
```

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://github.com/mwardRH/blueflask.git
```
