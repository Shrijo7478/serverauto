from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory product list
products = []

@app.route('/')
def home():
    return jsonify({"message": "Backend is running"}), 200

# Get all products
@app.route('/product', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Add a new product
@app.route('/product', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        if not data or 'id' not in data:
            return jsonify({"error": "Invalid product data"}), 400
        products.append(data)
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a product by ID
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p.get('id') != product_id]
    return jsonify({"message": f"Product with ID {product_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)