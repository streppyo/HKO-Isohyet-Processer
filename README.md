# HKO Isohyet Processor

Flask application that serve PNG. Pre-processed isohyet chart (provided by HKO) with colours mapped to a purple colour gradient.

## Requirements and rationale
Python with cv2 (used to process image), requests, flask package installed
Upon receiving a HTTP GET request of the correct path (http://localhost:5000/weather/isohyet?date=MMDD) which have to be changed according to your config, the program downloads isohyet chart from HKO website, process it and save it to the local project directory. Subsequently the PNG is served.

## Effect

Raw file:

![alt text](https://github.com/streppyo/hko_isohyet_processer/blob/5ca4fd801e3ac11add5acd8f6048732497b01b66/hko_isohyet_processer/_src/rfmap24hrs07210000e.png)

Processed:

![alt text](https://github.com/streppyo/hko_isohyet_processer/blob/5ca4fd801e3ac11add5acd8f6048732497b01b66/hko_isohyet_processer/static/images/0721.png)

## Files

- hkoiso.py

.py file that constructs layers and data for parsing isohyet layer

- main.py

.py the main programme that processed the image based on hkoiso.py

- host.py

The Flask wrapper that call the program in main.py and responses to GET requests
