# kms-checker-api
A very simple way to check if a kms server is available and return information about it in JSON.  Requires vlmcs.
# How to use:  
1. Fill in the path of vlmcs in check.py and run it;  
2. Send a GET request to http://127.0.0.1:5000/check with the following parameters:  
[Required] server - The address of the KMS server to be detected can be IPv4, IPv6 or domain name;  
[Optional] port - Port number 1688 is used by default.  If you need to specify manually, please provide this parameter.
# To do:  
- Allow specifying IPv4 or IPv6 for domain names
- Display the test time when the test is successful
# Example responses:
*GET https://vlmcs.ap.icu/check?server=win.kms.pub*  
**{"address":"[2605:6400:30:fa07:fa07:fa07:fa07:fa07]:1688","available":true,"port":1688,"server":"win.kms.pub","time":"2023-04-05 01:08:26"}**  
  
*GET https://vlmcs.ap.icu/check?server=win.kms.pub&port=22*  
**{"address":"N/A","available":false,"port":"22","server":"win.kms.pub","time":"2023-04-05 01:18:52"}**  
  
*GET https://vlmcs.ap.icu/check?server=2605:6400:30:fa07:fa07:fa07:fa07:fa07*  
**{"address":"[2605:6400:30:fa07:fa07:fa07:fa07:fa07]:1688","available":true,"port":1688,"server":"2605:6400:30:fa07:fa07:fa07:fa07:fa07","time":"2023-04-05 01:08:29"}**  
  
*GET https://vlmcs.ap.icu/check?server=20.118.99.224*  
**{"address":"20.118.99.224:1688","available":true,"port":1688,"server":"20.118.99.224","time":"2023-04-05 01:23:30"}**  
  
*GET https://vlmcs.ap.icu/check?server=random*  
**{"error":"random is not a valid IP address or domain name"}**  
  
*GET https://vlmcs.ap.icu/check?port=11*  
**{"error":"Server parameter is required"}**  

