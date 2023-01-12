from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Connect to Redis container
r = redis.Redis(host='redis', port=6379, db=0)
# # Store a key-value pair
r.set('Devops', 'Kwami')
@app.route('/', methods=['GET'])
def get_value():
    key = 'Devops'
    # Get value from Redis by key
    value = r.get(key)

    # Return value as JSON
    if value:
        return jsonify({'DevOps_Engineer': value.decode()})
    else:
        return jsonify({'error': 'Key not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)