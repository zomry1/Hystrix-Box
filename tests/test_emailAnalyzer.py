from Tools.emailAnalyzer import email_analyzer

TEXT = ("Subject: Coming Wednesday, April 1st... Nailed It! Season 4\n"
        "Date: Tue, 24 Mar 2020 18:02:10 +0000\n"
        "From: Netflix <info@mailer.netflix.com>\n"
        "To: JohnSmlth@hotmail.com\n"
        "Message-ID: <010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@email.amazonses.com>\n"
        "List-Unsubscribe: <mailto:S0VXTkIzSUUyRkMzTkMyQ05KWktVSzZHRUFDNURF@unsubscribe.netflix.com>, "
        "<https://www.netflix.com/EmailUnsubscribe?id=BQE0AAEBENqyIWqRNrh%2B7"
        "%2FV5HCi4iKmAgHeFZDEnVSyIsgyi0afmQoJVpj1JX60NWdqEnhgc3v9rrhZtAXKmQ753EK64gUYakH9o2rLLGZ8FOuUc7NFjeE8eVPV1VNWyPgpBek7I3PeXlxgnc7bKneIOw51NZHKVY89Q%2BChey9LRE13FZe4%2Bo5C3KPNazPc%2BK7TzskJElw15&lnktrk=EMP&g=6A5F6B01C976E12BCF1F50C0AA5062A9645262CD&lkid=unsubscribe_link>\n"
        "Return-Path: \n"
        " 010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@mailer.netflix.com\n"
        "Content-Type: multipart/alternative; \n"
        "	boundary=\"----=_Part_87580_587082350.1585072930404\"\n"
        "Received: from VI1EUR04HT047.eop-eur04.prod.protection.outlook.com\n"
        " (2603:10b6:208:51::34) by MN2PR05MB6573.namprd05.prod.outlook.com with HTTPS\n"
        " via BL0PR02CA0093.NAMPRD02.PROD.OUTLOOK.COM; Tue, 24 Mar 2020 18:02:12 +0000\n"
        "Received: from VI1EUR04FT022.eop-eur04.prod.protection.outlook.com\n"
        " (2a01:111:e400:7e0e::33) by\n"
        " VI1EUR04HT047.eop-eur04.prod.protection.outlook.com (2a01:111:e400:7e0e::349)\n"
        " with Microsoft SMTP Server (version=TLS1_2,\n"
        " cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.2814.13; Tue, 24 Mar\n"
        " 2020 18:02:11 +0000\n"
        "Received: from a41-20.smtp-out.amazonses.com (75.117.114.116) by\n"
        " VI1EUR04FT022.mail.protection.outlook.com (10.152.28.70) with Microsoft SMTP\n"
        " Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id\n"
        " 15.20.2814.13 via Frontend Transport; Tue, 24 Mar 2020 18:02:10 +0000\n")


def test_email_analyzer_email():
    assert (email_analyzer('../examples/emailAnalyzer.eml') == TEXT)


def test_email_analyzer_text_file():
    assert (email_analyzer('../examples/extractor.txt') == '')


def test_strings_noFile():
    assert (email_analyzer('') == '')


def test_email_analyzer_image_file():
    assert (email_analyzer('../examples/LSBimage.png') == '')