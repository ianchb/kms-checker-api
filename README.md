# kms-checker-api
A very simple way to check if a kms server is available and return information about it in json.  Requires vlmcs.
# How to use:  
1. Fill in the path of vlmcs in check.py and run it;  
2. Send a GET request to http://127.0.0.1:5000/check with the following parameters:  
[Required] server - The address of the KMS server to be detected can be IPv4, IPv6 or domain name;  
[Optional] port - Port number 1688 is used by default.  If you need to specify manually, please provide this parameter.
