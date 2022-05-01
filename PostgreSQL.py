import jaydebeapi as jdbc

#sql = 'Select * From world.city'
postgresql_class = 'org.postgresql.Driver'
postgresql_jdbc_path = 'lib/postgresql-42.3.4.jar'
postgresql_url = 'jdbc:postgresql://localhost:5432/'
postgresql_user = 'postgres'
postgresql_pw = 'LOTTI007'

conn = jdbc.connect(postgresql_class,
                    postgresql_url,
                    [postgresql_user, postgresql_pw],
                    postgresql_jdbc_path)

curs = conn.cursor()


#SQL
createDB = 'CREATE DATABASE "db2-1"'

#create DB
try:
    curs.execute(createDB)
except:
    print("DB may exists already")


#

#curs.execute('SELECT * FROM csv_reports LIMIT 2')
#curs.fetchall()
curs.close()
conn.close()