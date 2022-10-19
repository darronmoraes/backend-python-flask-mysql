from app import app
from flaskext.mysql import MySQL

# MYSQL object
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'rds-numino.czuxz43ipobf.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'numino'
mysql.init_app(app)