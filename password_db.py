import sqlite3


class DbPasswords:


    def connect_to_db(self):
        connection = sqlite3.connect('password_record.db')
        return connection
    
    def create_table(self, table_name="password_info"):
        connection = self.connect_to_db()
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            website TEXT NOT NULL,
            username VARCHAR(100),
            password VARCHAR(50)
        );
        '''

        with connection as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            
    def create_record(self, data, table_name="password_info"):
        website = data['website']
        username = data['username']
        password = data['password']
        connection = self.connect_to_db()
        query = f'''
        INSERT INTO {table_name}('website', 'username', 'password') VALUES (?, ?, ?);
        '''
        

        with connection as connection:
            cursor = connection.cursor()
            cursor.execute(query, (website, username, password))
            
    
    def show_records(self, table_name="password_info"):
        connection = self.connect_to_db()
        query = f'''
        SELECT * FROM {table_name};
        '''


        with connection as connection:
            cursor = connection.cursor()
            list_records = cursor.execute(query)
            return list_records
        
    def update_record(self, data, table_name="password_info"):
        ID = data['ID']
        website = data['website']
        username = data['username']
        password = data['password']
        connection = self.connect_to_db()
        query = f'''
        UPDATE {table_name} SET website= ?, username=?, password=? WHERE ID= ?;
        '''


        with connection as connection:
            cursor = connection.cursor()
            cursor.execute(query, (website, username, password, ID))
                
    def delete_record(self, ID, table_name="password_info"):
        
        connection = self.connect_to_db()
        query = f'''
        DELETE FROM {table_name} WHERE ID= ?;
        '''


        with connection as connection:
            cursor = connection.cursor()
            cursor.execute(query, (ID,))
                