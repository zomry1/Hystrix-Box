Extractor Module
================

Ultimate Extractor, extract information from given data

.. admonition:: Usage

    ``[-h] [--version] [-v] [-o FILENAME] [-e EXTRACTOR] filename``

Arguments
---------

Positional Arguments
~~~~~~~~~~~~~~~~~~~~
:Filename:
    :Type: *str*
    :Aliases: ``--filename``
    :Explenation: Set path for file to be read for extracting


Optional Arguments
~~~~~~~~~~~~~~~~~~
:-h:
    :Type: *flag*
    :Aliases: ``--help``
    :Expleneation: Show help message and exit

:--version:
    :Type: *flag*
    :Expleneation: Show the version of the tool

:-v:
    :Type: *flag*
    :Aliases: ``--verbose``
    :Expleneation: Verbose mode, printing additional information

:-o Filename:
    :Type: *str*
    :Aliases: ``--output``
    :Expleneation: Path for the file the results will be saved in

:-e Extractor:
    :Type: *str*
    :Default: all
    :Options: ascii, base64, caesar, reverse, hash
    :Aliases: ``--extractor``
    :Expleneation: Use specific extractor


Examples
--------

- Using data.txt file and use all extractors:

    .. code-block:: console

        >>> data.txt


- Using data.txt file and use only email extractor:

    .. code-block:: console

        >>> data.txt -e email

- Using data.txt file and extract only url to urls.txt file:

    .. code-block:: console

        >>> code.txt -o urls.txt

