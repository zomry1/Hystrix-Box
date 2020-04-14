Decrypter Module
================

Ultimate Decrypter, decrypt the given ciphertext by all known decoders.
Evaluate each result and return the best result.

.. admonition:: Usage

    ``[-h] (-c CIPHERTEXT | -f FILENAME) [--version] [-s DECODER] [-cl] [-cw] [-cf FORMAT]``
    ``[-n NUMBER] [-v] [-o FILENAME]``

Arguments
---------

Positional Arguments
~~~~~~~~~~~~~~~~~~~~
:-f Filename:
    :Type: *str*
    :Aliases: ``--filename``
    :Explenation: Set path for file to be decrypted

`or`

:-c Ciphertext:
    :Type: *str*
    :Aliases: ``--ciphertext``
    :Explenation: Paste ciphertext


Optional Arguments
~~~~~~~~~~~~~~~~~~
:-h:
    :Type: *flag*
    :Aliases: ``--help``
    :Expleneation: Show help message and exit

:--version:
    :Type: *flag*
    :Expleneation: Show the version of the tool

:-d:
    :Type: *str*
    :Options: ascii, base64, caesar, reverse, hash
    :Aliases: ``--decoder``
    :Expleneation: Use specific decoder

:-n Number:
    :Type: *int*
    :Default: 1
    :Aliases: ``--number``
    :Expleneation: Number of results to be printed (sorted by descending score)


.. Note::
    If none from below is selected, the script uses all the evaluators together

:-cl:
    :Type: *flag*
    :Aliases: ``--checkLetter``
    :Expleneation: Use letter analysis to evaluate the results

:-cw:
    :Type: *flag*
    :Aliases: ``--checkWord``
    :Expleneation: Use word analysis to evaluate the results

:-cf Format:
    :Type: *str*
    :Aliases: ``--checkLetter``
    :Expleneation: Search the CTF flag to evaluate the results

.. important::

    If the CTF normal flag is omryCTF2020{XXXXXXXXXXXXXXX}

    you need to enter: ``omryCTF2020{}``

:-v:
    :Type: *flag*
    :Aliases: ``--verbose``
    :Expleneation: Verbose mode, printing additional information

:-o Filename:
    :Type: *str*
    :Aliases: ``--output``
    :Expleneation: Path for the file the results will be saved in


Examples
--------

- Using code.txt file and use all evaluators:

    .. code-block:: console

        >>> -f code.txt


- Using code.txt file and use letter analysis evaluator:

    .. code-block:: console

        >>> -f code.txt -cl

- Decrypt string and use Base64 decoder:

    .. code-block:: console

        >>> -c VGhpcyBpcyBhbiBleGFtcGxlIQ== -d base64

.. important::

    When using -c flag, when the ciphertext has whitespaces in it, the argument should be written between quotation marks ``"``

- Decrypt string (with whitespaces in it) and use flag evaluator:

    .. code-block:: console

        >>> -c "}wonK_tnoD_I{0202FTCyrmo galf ym si erehW" -cf omryCTF2020{}


- Using code.txt file, return the top 5 results and save it in results.txt file :

    .. code-block:: console

        >>> -f code.txt -n 5 -o results.txt


