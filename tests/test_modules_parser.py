import filecmp
import os

from HystrixBox.modules_parser import decrypter_module, file_module, strings_module, zip_extract_module, emailAnalyzer_module, \
    extractor_module

TEST1 = '''[1] Result: Perhaps the most well-publicized tech tool in Russia's arsenal for fighting coronavirus is Moscow's massive facial-recognition system. Rolled out earlier this year, the surveillance system had originally prompted an unusual public backlash, with privacy advocates filing lawsuits over unlawful surveillance.
Coronavirus, however, has given an unexpected public-relations boost to the system.
Last week, Moscow police claimed to have caught and fined 200 people who violated quarantine and self-isolation using facial recognition CTF2020{DSADASDASDAS} and a 170,000-camera system. According to a Russian media report some of the alleged violators who were fined had been outside for less than half a minute before they were picked up by a camera.
"We want there to be even more cameras so that that there is no dark corner or side street left," Oleg Baranov, Moscow's police chief, said in a recent briefing, adding that the service is currently working to install an additional 9,000 cameras.\n\n'''

TEST2 = 'File extension: bmp\nother extensions names: \nMIME: image/bmp\ndescription: Windows (or device-independent) bitmap image'

TEST3 = '''ICC_PROFILE
mntrRGB XYZ 
DDDDDDDDDEI
}DDDDDDDDDDV.
YqU""""""""""""""""""""""""""*D
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE
"""""""""""""""""""""""""*H
"""""""""/>d
DDDDDDDDEl)
DDDDDDDDDD^9
DDDDDDDDDDV'''

TEST5 = '''Subject: Coming Wednesday, April 1st... Nailed It! Season 4
Date: Tue, 24 Mar 2020 18:02:10 +0000
From: Netflix <info@mailer.netflix.com>
To: JohnSmlth@hotmail.com
Message-ID: <010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@email.amazonses.com>
List-Unsubscribe: <mailto:S0VXTkIzSUUyRkMzTkMyQ05KWktVSzZHRUFDNURF@unsubscribe.netflix.com>, <https://www.netflix.com/EmailUnsubscribe?id=BQE0AAEBENqyIWqRNrh%2B7%2FV5HCi4iKmAgHeFZDEnVSyIsgyi0afmQoJVpj1JX60NWdqEnhgc3v9rrhZtAXKmQ753EK64gUYakH9o2rLLGZ8FOuUc7NFjeE8eVPV1VNWyPgpBek7I3PeXlxgnc7bKneIOw51NZHKVY89Q%2BChey9LRE13FZe4%2Bo5C3KPNazPc%2BK7TzskJElw15&lnktrk=EMP&g=6A5F6B01C976E12BCF1F50C0AA5062A9645262CD&lkid=unsubscribe_link>
Return-Path: 
 010001710db57e6f-f9850d85-346e-4249-9551-71042c80ff5b-000000@mailer.netflix.com
Content-Type: multipart/alternative; 
\tboundary="----=_Part_87580_587082350.1585072930404"
Received: from VI1EUR04HT047.eop-eur04.prod.protection.outlook.com
 (2603:10b6:208:51::34) by MN2PR05MB6573.namprd05.prod.outlook.com with HTTPS
 via BL0PR02CA0093.NAMPRD02.PROD.OUTLOOK.COM; Tue, 24 Mar 2020 18:02:12 +0000
Received: from VI1EUR04FT022.eop-eur04.prod.protection.outlook.com
 (2a01:111:e400:7e0e::33) by
 VI1EUR04HT047.eop-eur04.prod.protection.outlook.com (2a01:111:e400:7e0e::349)
 with Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.2814.13; Tue, 24 Mar
 2020 18:02:11 +0000
Received: from a41-20.smtp-out.amazonses.com (75.117.114.116) by
 VI1EUR04FT022.mail.protection.outlook.com (10.152.28.70) with Microsoft SMTP
 Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id
 15.20.2814.13 via Frontend Transport; Tue, 24 Mar 2020 18:02:10 +0000
'''

TEST6 = '''Extract url:
gmail.com
http://www.google.com
124.27.1.1

Extract ip:
124.27.1.1

Extract email:
null@gmail.com

Extract md5:
No result found

'''


def compareDir(dir1, dir2):
    """
        Compare two directory trees content.
        Return False if they differ, True is they are the same.
        """
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files
            or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not compareDir(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True


def test_decrypter_module(capfd):
    assert (decrypter_module(['-f', '../examples/decrypter.txt']) == TEST1)


def test_file_module():
    assert (file_module(['../examples/DetectFileFormat/BMP.BMP']) == TEST2)


'''
def test_strings_module():
    assert (strings_module(['../examples/strings.jpg', '-n', '11']) == TEST3)
'''


def test_zip_extract_module(tmpdir):
    path = tmpdir.strpath
    assert (zip_extract_module(['../examples/recursivezip.zip', '-p', path]) == 'Done extracting' and
            compareDir(path, '../examples/RecursiveZipExtracted/'))


def test_email_analyzer_module():
    assert (emailAnalyzer_module(['../examples/emailAnalyzer.eml']) == TEST5)


def test_extractor_module():
    assert (extractor_module(['../examples/extractor.txt']) == TEST6)
