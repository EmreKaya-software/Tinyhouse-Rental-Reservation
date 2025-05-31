from flask import Flask, request,jsonify, Response
import json
from flask_cors import CORS

from db_config import get_db_connection

app = Flask(__name__)
CORS(app)


# 1. Kullanıcı Ekleme
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC usp_AddUser ?, ?, ?, ?, ?", (name, surname, email, password, role))
        conn.commit()
        conn.close()
        return Response(json.dumps({'message': 'Kullanıcı başarıyla eklendi!'}, ensure_ascii=False), mimetype='application/json', status=201)
    except Exception as e:
        return Response(json.dumps({'error': str(e)}, ensure_ascii=False), mimetype='application/json', status=500)

# 2. Belirli evin rezervasyonlarını listele
@app.route('/get_reservations_by_house', methods=['GET'])
def get_reservations_by_house():
    house_id = request.args.get('house_id')

    if not house_id:
        return Response(json.dumps({'error': 'house_id parametresi gerekli!'}, ensure_ascii=False), mimetype='application/json', status=400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC usp_GetReservationsByHouse @house_id = ?", (house_id,))
        rows = cursor.fetchall()
        conn.close()

        reservations = []
        for row in rows:
            reservations.append({
                'reservation_id': row[0],
                'renter_name': row[1],
                'start_date': str(row[2]),
                'end_date': str(row[3]),
                'status': row[4]
            })

        return Response(json.dumps(reservations, ensure_ascii=False), mimetype='application/json', status=200)

    except Exception as e:
        return Response(json.dumps({'error': str(e)}, ensure_ascii=False), mimetype='application/json', status=500)

# 3. Ev Ekleme
@app.route('/add_house', methods=['POST'])
def add_house():
    data = request.get_json()
    owner_id = data.get('owner_id')
    title = data.get('title')
    description = data.get('description')
    location = data.get('location')
    price_per_night = data.get('price_per_night')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC usp_AddHouse ?, ?, ?, ?, ?", (owner_id, title, description, location, price_per_night))
        conn.commit()
        conn.close()
        return Response(json.dumps({'message': 'Ev başarıyla eklendi!'}, ensure_ascii=False), mimetype='application/json', status=201)
    except Exception as e:
        return Response(json.dumps({'error': str(e)}, ensure_ascii=False), mimetype='application/json', status=500)
#4. giriş yapma
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, surname, role FROM Users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return jsonify({
                'message': 'Giriş başarılı!',
                'user_id': user[0],
                'name': user[1],
                'surname': user[2],
                'role': user[3]
            }), 200
        else:
            return jsonify({'error': 'Geçersiz e-posta veya şifre!'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#5 rezervasyon yapma
@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    data = request.get_json()
    house_id = data['house_id']
    renter_id = data['renter_id']
    start_date = data['start_date']
    end_date = data['end_date']
    status = data['status']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC usp_MakeReservation ?, ?, ?, ?, ?",
                       (house_id, renter_id, start_date, end_date, status))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Rezervasyon başarıyla eklendi.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#6 bütün evleri listeleme
@app.route('/get_all_houses', methods=['GET'])
def get_all_houses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC usp_GetAllHouses")
        rows = cursor.fetchall()
        conn.close()

        houses = []
        for row in rows:
            houses.append({
                'house_id': row[0],
                'title': row[1],
                'location': row[2],
                'price_per_night': float(row[3]),
                'description': row[4]
            })


        return jsonify(houses), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Sunucuyu başlat
if __name__ == '__main__':
    app.run(debug=True)
