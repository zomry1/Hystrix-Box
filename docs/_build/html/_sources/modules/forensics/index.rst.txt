Forensics Module
================

| The Forensics module built from bunch of tools.
| (Maybe in the future there will be an automated tool - an **Ultimate tool**)

add image here

| All those tools has the default args of

 * ``-h`` = help
 * ``--version`` = print tool version
 * ``-v`` = verbose mode
 * ``-o Filename`` = save the result in output file

| From now and on I will not describe those flags in this section.

Tools
-----
 * :ref:`file_label`
 * :ref:`strings_label`
 * :ref:`recursive_label`
 * :ref:`email_label`


.. _file_label:

Detect file type
~~~~~~~~~~~~~~~~
Determine the type of a file by his header (*magic number*)

.. note:: Like 'file' command in Unix

.. admonition:: Usage

    ``[-h] [--version] [-v] [-o FILENAME] filename``

Arguments
^^^^^^^^^

Only regular args.


Examples
^^^^^^^^^

- Check 'checkme' file (png file):

    .. code-block:: console

        >>> checkme
        File extension: png
        other extensions names:
        MIME: image/png
        description: Portable Network Graphics file

Code
^^^^




.. _strings_label:

Printable strings in file
~~~~~~~~~~~~~~~~~~~~~~~~~
Find printable strings in binary files

.. note:: Like 'strings' command in Unix

.. admonition:: Usage

    ``[-h] [--version] [-v] [-o FILENAME] [-n NUMBER] filename``

Arguments
^^^^^^^^^

Optional Arguments
####################
:-n Number:
    :Type: *int*
    :Expleneation: Print only sequences of characters that are at least min-len of this number
    :Default: 4

Examples
^^^^^^^^^

- Search in 'checkme' file:

    .. code-block:: console

        >>> checkme
        Strings will be printed here

- Search in 'longwords'  for strings at least 10 characters long:

    .. code-block:: console

        >>> checkme -n 10
        Strings will be printed here

Code
^^^^


.. _recursive_label:

Recursive Decompression
~~~~~~~~~~~~~~~~~~~~~~~
Decompress nested zip files, saves the files hierarchy (nested zips changed to directories).

.. admonition:: Usage

    ``[-h] [--version] [-v] [-o FILENAME] [-p PATH] filename``

Arguments
^^^^^^^^^

Optional Arguments
####################
:-p Path:
    :Type: *str*
    :Expleneation: Set path to extract the zip files
    :Default: Current directory

Examples
^^^^^^^^^

- Extract nested.zip file to current directory

    .. code-block:: console

        >>> nested.zip

- Extract nested.zip file to directory named 'Data' in the current directory

    .. code-block:: console

        >>> nested.zip -p Data

Code
^^^^


.. _email_label:

Email analyzer
~~~~~~~~~~~~~~
Analyze email file headers to extract important information

* Subject
* Data
* From
* To
* Message-ID
* Unsubscribe URL
* Return Path (The email address when replying to this message)
* Content-Type (Check for attached files)
* Received (All the station the email pass through, track the sender)

.. admonition:: Usage

    ``[-h] [--version] [-v] [-o FILENAME] filename``

Arguments
^^^^^^^^^

Only regular args

Examples
^^^^^^^^^

- Analyze email file with the name sendme.eml

    .. code-block:: console

        >>> sendme.eml
        Subject: Coming Wednesday, April 1st... Nailed It! Season 4
        Date: Tue, 24 Mar 2020 18:02:10 +0000
        From: Netflix <info@mailer.netflix.com>
        To: JohnSmlth@hotmail.com
        Message-ID: <010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@email.amazonses.com>
        List-Unsubscribe: <mailto:S0VXTkIzSUUyRkMzTkMyQ05KWktVSzZHRUFDNURF@unsubscribe.netflix.com>, <https://www.netflix.com/EmailUnsubscribe?id=BQE0AAEBENqyIWqRNrh%2B7%2FV5HCi4iKmAgHeFZDEnVSyIsgyi0afmQoJVpj1JX60NWdqEnhgc3v9rrhZtAXKmQ753EK64gUYakH9o2rLLGZ8FOuUc7NFjeE8eVPV1VNWyPgpBek7I3PeXlxgnc7bKneIOw51NZHKVY89Q%2BChey9LRE13FZe4%2Bo5C3KPNazPc%2BK7TzskJElw15&lnktrk=EMP&g=6A5F6B01C976E12BCF1F50C0AA5062A9645262CD&lkid=unsubscribe_link>
        Return-Path:
         010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@mailer.netflix.com
        Content-Type: multipart/alternative;
            boundary="----=_Part_87580_587082350.1585072930404"
        Received: from VI1EUR04HT047.eop-eur04.prod.protection.outlook.com
         (2603:10b6:208:51::34) by MN2PR05MB6573.namprd05.prod.outlook.com with HTTPS
         via BL0PR02CA0093.NAMPRD02.PROD.OUTLOOK.COM; Tue, 24 Mar 2020 18:02:12 +0000
        Received: from VI1EUR04FT022.eop-eur04.prod.protection.outlook.com
         (2a01:111:e400:7e0e::33) by
         VI1EUR04HT047.eop-eur04.prod.protection.outlook.com (2a01:111:e400:7e0e::349)
         with Microsoft SMTP Server (version=TLS1_2,
         cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.2814.13; Tue, 24 Mar
         2020 18:02:11 +0000

Code
^^^^

