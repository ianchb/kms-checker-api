from flask import Flask, jsonify, request
import re
import os
import time
import socket
app = Flask(__name__)
def is_valid_kms_server(kms_server):
    try:
        socket.inet_pton(socket.AF_INET, kms_server)
        return True, 'IPv4'
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, kms_server)
            return True, 'IPv6'
        except socket.error:
            try:
                socket.gethostbyname(kms_server)
                return True, 'domain'
            except socket.gaierror:
                return False, ''
vlmcs_path = "" #Please fill in the path to the vlmcs. For example: /home/vlmcs
@app.route('/check', methods=['GET'])
def check_kms_server():
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    kms_server = request.args.get('server')
    kms_port = request.args.get('port') or 1688
    if not kms_server:
        return jsonify({'error': 'Server parameter is required'})
    valid, server_type = is_valid_kms_server(kms_server)
    if not valid:
        return jsonify({'error': f'{kms_server} is not a valid IP address or domain name'})
    else:
        if server_type == "IPv6":
            kms_server = f"[{kms_server}]"
        address, result = check_kms_server_available(kms_server, kms_port)
        if server_type == "IPv6":
            kms_server = kms_server.replace("[","",1).replace("]","",1)
        return jsonify({'time': tm, 'available': result, 'address': address, 'server': kms_server, 'port': kms_port})
def check_kms_server_available(kms_server, kms_port):
    with os.popen(f"{vlmcs_path} -l8 {kms_server}:{kms_port}") as output:
        first_line = output.readline()
    word = "successful"
    if word in first_line:
        match = re.search(r'Connecting to (.+?) \.\.\. successful', first_line)
        if match:
            address = match.group(1)
            return address, True
    else:
        return "N/A", False
if __name__ == '__main__':
    app.run(debug=False, port=5000)
