from time import sleep
import requests, re


def get_gecode_from_coordinate(match):
    lat = match.group(1)
    long = match.group(2)
    r = requests.get("https://geocode.xyz/{},{}?json=1".format(lat, long))
    sleep(1) # The server accept 1 request each second
    j = r.json()
    geocode = 'GeoCode not found'
    try:
        geocode = j['geocode']
    finally:
        return geocode


def CoordinatesCipher(ciphertext):
    result = ''
    coordinate = None
    for coordinate in re.finditer(r'\(([\d\.-]+), ([\d\.-]+)\)', ciphertext):
        result += get_gecode_from_coordinate(coordinate) + '\n'

    if coordinate is None: #Nothing found
        return []
    return result


#TEXT = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

#print(CoordinatesCipher(TEXT))