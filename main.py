from ast import Str
import jsonpickle
import pymysql
from app import app
from config import mysql
from flask import jsonify, request
from flask import flash, Request

@app.route('/create', methods=['POST'])
def create_student():
    con = None
    curs = None
    try:
        _json = request.json
        _first_name = _json['first_name']
        _last_name = _json['last_name']
        _gender = _json['gender']
        _email = _json['email']
        _country = _json['country']
        _mobile = _json['mobile']
        if _first_name and _last_name and _gender and _email and _country and _mobile:
            # con = mysql.connect()
            # curs = con.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO student(first_name, last_name, gender, email, country, mobile) VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (_first_name, _last_name, _gender, _email, _country, _mobile)
            con = mysql.connect()
            curs = con.cursor()
            curs.execute(sqlQuery, bindData)
            con.commit()
            response = jsonify('Student added successfully')
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
        cursor.execute("SELECT * FROM student")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/user/<string:first_name>')
def get_user(first_name):
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student WHERE first_name = %s", first_name)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/update/<string:first_name>', methods=['PUT'])
def update_user(first_name):
    try:
        _json = request.json
        _first_name = _json['first_name']
        _last_name = _json['last_name']
        _email = _json['email']
        _mobile = _json['mobile']
        if _first_name and _last_name and _email and _mobile:
            sqlQuery = "UPDATE student SET first_name = %s, last_name = %s, email = %s, mobile = %s WHERE first_name = %s"
            bindData = ( _first_name, _last_name, _email, _mobile, first_name)
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            con.commit()
            response = jsonify('Student updated successfully')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/delete/<string:first_name>', methods=['DELETE'])
def delete_user(first_name):
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM student WHERE first_name = %s", (first_name))
        con.commit()
        response = jsonify('Student deleted successfully')
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