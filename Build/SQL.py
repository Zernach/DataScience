import sqlite3


class SQL:
    '''Use this to run SQL commands without all the hassel.'''
    
    def __init__(self, sql):
        '''SQL init'''
        self.dbpath = sql
        self.conn   = sqlite3.connect(sql)
    
    
    def query(self, query):
        '''SQL commands
        Also, a 'cursor' in SQL is essentially a copy of the part of the dataframe being worked on, sort of like what pandas does.
        '''
        cursor = self.conn.cursor()
        result = cursor.execute(query).fetchall()
        cursor.close()
        self.conn.commit()
        return result