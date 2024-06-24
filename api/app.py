from flask import Flask, request, jsonify
import mysql.connector
import ssl

app = Flask(__name__)

# SSL/TLS configuration
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')

# MySQL Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql_host',
        user='mysql_user',
        password='mysql_password',
        database='discount_db'
    )
    return connection

@app.route('/discount', methods=['POST'])
def apply_discount():
    data = request.json
    product_id = data['product_id']
    discount_rate = data['discount_rate']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('UPDATE products SET discount_rate = %s WHERE id = %s', (discount_rate, product_id))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({'status': 'success', 'product_id': product_id, 'discount_rate': discount_rate})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
