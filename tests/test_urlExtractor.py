from Extractors.urlExtractor import URLExtractor

TEXT = '''add1 http://mit.edu.com abc
add2 https://facebook.jp.com.2. abc
add3 www.google.be. uvw
add4 https://www.google.be. 123
add5 www.website.gov.us test2
Hey bob on www.test.com. 
another test with ipv4 http://192.168.1.1/test.jpg. toto2
website with different port number www.test.com:8080/test.jpg not port 80
www.website.gov.us/login.html
test with ipv4 (192.168.1.1/test.jpg).
search at google.co.jp/maps.
test with ipv6 2001:0db8:0000:85a3:0000:0000:ac1f:8001/test.jpg.
'''
def test_extract():
    assert URLExtractor.extract(TEXT) == ['http://mit.edu.com', 'https://facebook.jp.com', 'www.google.be',
                                          'https://www.google.be', 'www.website.gov.us', 'www.test.com',
                                          'http://192.168.1.1/test.jpg','www.test.com:8080/test.jpg',
                                          'www.website.gov.us/login.html',  '192.168.1.1/test.jpg', 'google.co.jp/maps',
                                          '2001:0db8:0000:85a3:0000:0000:ac1f:8001/test.jpg']