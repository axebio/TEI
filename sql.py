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

def create_tables():
    connection = connect()

    tb_user = '''CREATE TABLE IF NOT EXISTS tb_user
                        (usuario    VARCHAR(20),
                        senha       VARCHAR(12),
                        CONSTRAINT pk_tb_user PRIMARY KEY(usuario)
                        );
                        '''


    tb_clientes = '''CREATE TABLE IF NOT EXISTS tb_clientes
                        (id_cliente             NUMERIC(5),
                        nome_cliente            VARCHAR(20),
                        tel_cliente             NUMERIC(11),
                        email_cliente           VARCHAR(30),
                        end_cliente             VARCHAR(50),
                        CONSTRAINT pk_tb_cliente PRIMARY KEY(id_cliente)
                        );
                        '''

    tb_produtos = '''CREATE TABLE IF NOT EXISTS tb_produtos
                        (id_prod                     NUMERIC(5),
                        nome_prod                    VARCHAR(30),
                        p_compra_prod                NUMERIC(5),
                        p_venda_prod                 NUMERIC(5),
                        quant_prod                   NUMERIC(4),
                        CONSTRAINT pk_tb_produtos PRIMARY KEY(id_prod)
                        );
                        '''

    cur = connection.cursor()

    tables = [tb_user, tb_clientes, tb_produtos]
    for i in tables:
        cur.execute(i)

    connection.commit()
    connection.close()

def insert_data(table, values):
    connection = connect()
    cur = connection.cursor()

    if (table == "tb_user"):
        tb_user = '''INSERT INTO tb_user (usuario, senha)
                    VALUES ('{}', '{}');'''.format(
                        values[0], 
                        values[1])
        cur.execute(tb_user)
    
    elif (table == "tb_clientes"):
        tb_clientes = '''INSERT INTO tb_clientes
                    VALUES ('{}', '{}', '{}', '{}', '{}');'''.format(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4])
        cur.execute(tb_clientes)
    
    elif (table == "tb_produtos"):
        tb_produtos = '''INSERT INTO tb_produtos
                    VALUES ({}, {}, {}, {}, {});'''.format(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4])
        cur.execute(tb_produtos)



    connection.commit()
    connection.close()
    

	# Insert data into table



	


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

dados = [2, 3, 1, 2, 3]

# create_tables()
insert_data("tb_clientes", dados)