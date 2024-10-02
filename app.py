from flask import Flask, request, jsonify, render_template
from blockchain_model import Blockchain
from identity_data import IdentityData

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_identity', methods=['POST'])
def submit_identity():
    identity = request.form['identity']
    details = request.form['details']
    
    # Add identity to blockchain
    data = IdentityData(identity, details)
    block = blockchain.add_block(data.to_dict())
    
    return jsonify({
        'message': 'Identity added to blockchain!',
        'block': block.to_dict()
    })

@app.route('/verify_identity', methods=['POST'])
def verify_identity():
    identity = request.form['identity']
    
    # Verify identity on blockchain
    is_verified = blockchain.verify_identity(identity)
    
    return jsonify({
        'identity': identity,
        'verified': is_verified
    })

if __name__ == '__main__':
    app.run(debug=True)

