Hystrix-Box Tutorial
====================

.. note::
   This tutorial only cover the basic tools of ``Hystrix-Box``

Install and run Hystrix-Box
---------------------------

Install dependencies
~~~~~~~~~~~~~~~~~~~~~
Hystrix-Box supports Python 3.6 and above

To check whether you have an appropriate version of Python 3:

.. code-block:: console
   :linenos:

   $ python3 --version

If this does not return a version number or returns a version lower than 3.5, you will need to `install Python 3 <https://www.python.org/downloads/>`_

Install Hystrix-Box
~~~~~~~~~~~~~~~~~~~
Use pip, which is packaged with Python, to install Hystrix-Box and its dependencies:

.. code-block:: console
   :linenos:

   $ pip install hystrix-box

.. _Keys_label:

Add API keys
~~~~~~~~~~~~

| Open `HystrixBox/keys.py` and change the vars values corsponed to your API keys
| you got when registering to `Oxford Dictionaries <https://developer.oxforddictionaries.com>`_

Run Hystrix-Box
~~~~~~~~~~~~~~~
Open CMD and type:

.. code-block:: console

    $ Hystrix-Box

If everything worked, you should be see this:

.. image:: demo.jpg