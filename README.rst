====================================================
infapy - The Informatica Cloud SDK for Python
====================================================

|Version| 

Infapy is the Informatica Intelligent Cloud Services Software Development Kit (SDK) 
for Python, which allows Python developers to write software that makes use
of services like Informatica CDI, Informatica Cloud Administrator, Informatica Cloud Monitor,
Informatica CAI etc. You can find the latest, most
up to date, documentation at our `doc site`_ , including a list of
services that are supported.

.. _`doc site`: https://infapy.github.io
.. |Downloads| image:: https://img.shields.io/badge/infapy-v1.0.7-brightgreen
    :target: https://pypi.org/project/infapy/
    :alt: Downloads
.. |Version| image:: https://img.shields.io/badge/infapy-v1.0.7-brightgreen
    :target: https://pypi.org/project/infapy/
    :alt: Version

Getting Started
---------------
.. code-block:: sh

    $ pip install infapy

    
Using Infapy
~~~~~~~~~~~~~~
After installing infapy 

.. code-block:: python
  
  >>> import infapy
  >>> infapy.encrypt()
  Enter your user name: myInfaUser
  Enter your password: myInfaPasswd
    infa_access_key_id = gAAAAABhT2AUGrFWcXKs0-hCER85DEqHZh2ClRI0xc0gjOtFcWi_1esa9AkZt4k58Y5r2yEVl3sUF9oezTGE1tyF2knFXUX3Og==
    infa_secret_access_key = gAAAAABhT2AUZ70m68HbSX2Lc3Xa-VQjObWUi2wCSXTiXMtLIVapDxrfKNS5bBffu1N334jmqql7LYer_r-mcjj4EwoS8U44Xg==

Next, set up credentials (in e.g. ``~/.infa/credentials``):

.. code-block:: ini

    [default]
    infa_access_key_id = YOUR_KEY
    infa_secret_access_key = YOUR_SECRET
    
    [dev]
    infa_access_key_id = YOUR_KEY
    infa_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ``~/.infa/config``):

.. code-block:: ini

   [default]
   region = us
   
   [dev]
   region = em
    

Then, from a Python interpreter:

.. code-block:: python

    >>> import infapy
    >>> infaHandler = infapy.connect()
    or
    >>> infaHandler = infapy.connect(profile="dev")
    >>> v3 = infaHandler.v3()
    >>> securityLogs = v3.getSecurityLogs().getSecurityLogsForLastOneDay()
    >>> print(securityLogs)
            

Getting Help
------------

We use GitHub issues for tracking bugs and feature requests and might have limited
bandwidth to address them. Please use these community resources for getting
help:

* Ask a question on `Stack Overflow <https://stackoverflow.com/>`__ and tag it with `infapy <https://stackoverflow.com/questions/tagged/infapy>`__
* If it turns out that you may have found a bug, please `open an issue <https://github.com/infapy/infapy/issues/new>`__


Contributing
------------

We value feedback and contributions from our community. Whether it's a bug report, new feature, correction, or additional documentation, we welcome your issues and pull requests.


Maintenance and Support for SDK Major Versions
----------------------------------------------

Infapy was made generally available on 25-Sep-2021 and is currently in the full support phase of the availability life cycle.


More Resources
--------------

* `License <https://github.com/infapy/infapy/blob/main/LICENSE>`__

