import email


wantedFields = ['Subject', 'Date', 'From', 'To', 'Message-ID', 'List-Unsubscribe', 'Return-Path', 'Content-Type',
                'Received']


def email_analyzer(filename):
    """Analyze email file headers

    :param filename: The file to analyze
    :type filename: str

    :returns: List of important information from the email header
    :rtype: list

    """
    try:
        with open(filename) as file:
            result = ''
            msg = email.message_from_file(file)
            for field in wantedFields:
                for value in (msg.get_all(field) or []):
                    result += field + ": " + value + '\n'
            return result
    except FileNotFoundError:
        return ''
    except UnicodeDecodeError:
        return ''
