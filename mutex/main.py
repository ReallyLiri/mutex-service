from uwsgidecorators import lock
import time
import os
from flask import Flask

LOCK_TIMEOUT = int(os.environ.get('LOCK_TIMEOUT', default=600))

app = Flask(__name__)

lock_time = None


@lock
def _lock_req():
	global lock_time
	now = time.time()
	if lock_time is None:
		lock_time = now
		return True
	elif (now - lock_time) >= LOCK_TIMEOUT:
		lock_time = now
		return True
	return False


@app.route('/lock', methods=['PUT'])
def lock_req():
	success = _lock_req()
	if success:
		return "locked", 202
	return "unavailable", 409


@lock
def _unlock_req():
	global lock_time
	lock_time = None


@app.route('/unlock', methods=['PUT'])
def unlock_req():
	_unlock_req()
	return "unlocked", 202


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
