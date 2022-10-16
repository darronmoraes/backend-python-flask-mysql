from ast import Str
import jsonpickle
import pymysql
from app import app
from config import mysql
from flask import jsonify, request
from flask import flash, Request

@app.route('/create', methods=['POST'])
def create_student():
   
    try:
        _json = request.json
        _user_name = _json['user_name']
        _email = _json['email']
        con = mysql.connect()
        
        curs = con.cursor(pymysql.cursors.DictCursor)
        if _user_name and _email == 'POST':
            
            sqlQuery = "INSERT INTO users(user_name, email) VALUES(%s, %s)"
            bindData = (_user_name, _email)
            curs.execute(sqlQuery, bindData)
            con.commit()
            response = jsonify('Employee added successfully')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        curs.close()
        con.close()

@app.route('/user')
def show_student():
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/user/<string:user_name>')
def get_user(user_name):
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE user_name = %s", user_name)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/update', methods=['PUT'])
def update_user():
    try:
        _json = request.json
        _user_name = _json['user_name']
        _email = _json['email']
        if _user_name and _email == 'PUT':
            sqlQuery = "UPDATE users SET user_name = %s, email = %s"
            bindData = (_user_name, _email)
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            con.commit()
            response = jsonify('Employee updated successfully')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/delete/<string:user_name>', methods=['DELETE'])
def delete_user(user_name):
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM users WHERE user_name = %s", (user_name))
        con.commit()
        response = jsonify('Employee deleted successfully')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        "status": 404,
        "message": 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()