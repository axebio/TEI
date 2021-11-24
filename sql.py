import psycopg2


def connect():
    connection = psycopg2.connect(
        host = "ec2-3-221-24-14.compute-1.amazonaws.com",
        database = "dbcimbaajv8c3l",
        user = "cnucpvybbkkjsm",
        password = "d1a2f05ff9c28be1b7cc2321dc9bd6cfb4241ae1a1c9a903b59437f70083d7d3",
        port = "5432",
    )
    return connection

#configurando o postgres
def create_table(table, var_type):
    connection = connect()

    cur = connection.cursor()

    sql = "CREATE TABLE IF NOT EXISTS {} ({})".format(table, var_type)

    cur.execute(sql)

    connection.commit()
    connection.close()

def insert_data(table, var, values):
    connection = connect()

    cur = connection.cursor()

	# Insert data into table
    sql = '''INSERT INTO {} {} VALUES {}'''.format (table, var, values)

    cur.execute(sql)
	
    connection.commit()	
    connection.close()

def select_data(table, columns = "*"):
    connection = connect()

    cur = connection.cursor()

    #baixar valores do banco de dados
    sql = "SELECT {} FROM {}".format(table, columns)

    cur.execute(sql)
    records = cur.fetchall()

    output = ''

    # for record in records:
    #     output_label.config(text=f'{output}\n{record[0]} {record[1]}')
    #     output = output_label['text']

