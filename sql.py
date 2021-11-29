from pandas.io import sql
import psycopg2
import pandas as pd
import tkinter as tk


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
                        (id_user     VARCHAR(20),
                        senha       VARCHAR(12),
                        CONSTRAINT pk_tb_user PRIMARY KEY(id_user)
                        );
                        '''


    tb_clientes = '''CREATE TABLE IF NOT EXISTS tb_clientes
                        (id_clientes            INTEGER,
                        nome_cliente            VARCHAR(20),
                        tel_cliente             VARCHAR(11),
                        email_cliente           VARCHAR(30),
                        end_cliente             VARCHAR(50),
                        CONSTRAINT pk_tb_clientes PRIMARY KEY(id_clientes)
                        );
                        '''

    tb_produtos = '''CREATE TABLE IF NOT EXISTS tb_produtos
                        (id_produtos                     INTEGER,
                        nome_prod                        VARCHAR(30),
                        p_compra_prod                    VARCHAR(5),
                        p_venda_prod                     VARCHAR(5),
                        quant_prod                       VARCHAR(4),
                        CONSTRAINT pk_tb_produtos PRIMARY KEY(id_produtos)
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

    sql = ""
    sql = '''INSERT INTO {} VALUES ('''.format(table)
    for i in values:
        sql += ''' '{}', '''.format(i)
    sql = sql[:-2]
    sql += ");"

    cur.execute(sql)

    connection.commit()
    connection.close()
    

	# Insert data into table

def select_data(table, columns = "*"):
    connection = connect()
    create_tables()
    #baixar valores do banco de dados
    sql = '''SELECT {} FROM {} ;'''.format(columns, table)

    df = pd.read_sql_query(sql,connection)
    connection.commit()
    connection.close()

    return df

def delete_data(table, ID):
    connection = connect()
    cur = connection.cursor()
    
    id = 'id_' + table.split("_")[1]
    sql = '''DELETE FROM {} WHERE {} = {} '''.format(table, id, ID)

    cur.execute(cur.mogrify(sql))
    connection.commit()
    connection.close()

def verificar(user):
    connection = connect()
    create_tables()
    #baixar valores do banco de dados
    sql = '''SELECT senha FROM tb_user WHERE id_user = '{}';'''.format(user)

    cur = connection.cursor()
    cur.execute(sql)
    senha = cur.fetchone()
    senha = senha[0]
    connection.commit()
    connection.close()
    return senha

