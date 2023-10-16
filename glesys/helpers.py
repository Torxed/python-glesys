import urllib.request
import json
import base64

def get_request(endpoint):
	from .session import session

	credentials = base64.b64encode(f"{session['configuration'].credentials.user}:{session['configuration'].credentials.key}".encode())

	req = urllib.request.Request(f"{session['configuration'].network.host}{endpoint}")
	req.add_header('Accept', 'application/json; charset=utf-8')
	req.add_header('Authorization', f'Basic {credentials.decode()}')

	response = urllib.request.urlopen(req)
	response_data = json.loads(response.read().decode())

	return response_data


def post_request(endpoint, payload):
	from .session import session

	credentials = base64.b64encode(f"{session['configuration'].credentials.user}:{session['configuration'].credentials.key}".encode())

	req = urllib.request.Request(f"{session['configuration'].network.host}{endpoint}")
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	req.add_header('Authorization', f'Basic {credentials.decode()}')

	json_payload = json.dumps(payload).encode('utf-8')
	
	req.add_header('Content-Length', len(json_payload))
	response = urllib.request.urlopen(req, json_payload)

	response_data = json.loads(response.read().decode())

	return response_data