import pymysql


class DBConnect():

    def __init__(self):
        pass

    def __connect(self, db):

        host = '127.0.0.1'
        conn = pymysql.connect(host=host, port=3306, user='root', passwd='mysql', db=db)
        return conn

    def SELECT(self, db, query):
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))  # conver each value in string

            all_rows.append(row)

        return all_rows

        conn.close()    # closing the connection
        cur.close()    # clearing the cursor

    def UPDATE(self, db, query):
        conn = self.__connect(db)
        cur = conn.cursor()


        result = cur.execute(query)
        conn.commit()

        conn.close()  # closing the connection
        cur.close()  # clearing the cursor

        return result

