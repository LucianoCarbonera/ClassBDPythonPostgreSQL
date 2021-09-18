# -----------------------------------------------------------------------------+
#                                                   				  \
#  Classe para banco de dados PostgreSQL                        		          \
# Cacador, 25 de Junho de 2021                                                 \
# Luciano Carbonera                                                            \
# -----------------------------------------------------------------------------+
import psycopg2


class Db:

    def __init__(self, host, db):
        try:
            self._db = psycopg2.connect(host=host, database=db, user='postgres', password='postgres')
            print("Conexao com DB realizada com sucesso")
        except:
            print("Não foi possivel conectar ao banco de dados. Verifique as informações da conexão e tente novamente")

    def select(self, select):
        global result, cur
        try:
            cur = self._db.cursor()
        except:
            print("Não foi possivel iniciar conexão")
        try:
            cur.execute(select)
            result = cur.fetchall()
            print("Query Executada com sucesso")
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            print("Algo deu errado na consulta :(")

    def select_one(self, select):
        global result, cur
        try:
            cur = self._db.cursor()
        except:
            print("Não foi possivel iniciar conexão")
        try:
            cur.execute(select)
            result = cur.fetchone()
            cur.close()
            print("Query Executada com sucesso")
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            print("Algo deu errado na consulta :(")


    def update(self, sql):
        global cur
        try:
            cur = self._db.cursor()
        except:
            print("Não foi possivel iniciar conexão")

        try:
            cur.execute(sql)
            self._db.commit()
            print("Query Executada com sucesso")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self._db.rollback()
            print("Algo deu errado na manipulação  :(")

    def delete(self, sql):
        global cur
        try:
            cur = self._db.cursor()
        except:
            print("Não foi possivel iniciar conexão")

        try:
            cur.execute(sql)
            self._db.commit()
            print("Query Executada com sucesso")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self._db.rollback()
            print("Algo deu errado na exclusao dos dados :(")


    def insert(self, sql):
        global cur
        try:
            cur = self._db.cursor()
        except:
            print("Não foi possivel iniciar conexão")
        try:
            cur.execute(sql)
            self._db.commit()
            print("Query Executada com sucesso")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self._db.rollback()
            cur.close()
            return 1
















