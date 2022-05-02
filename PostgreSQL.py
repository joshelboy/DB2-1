import jaydebeapi as jdbc

# sql = 'Select * From world.city'
postgresql_class = 'org.postgresql.Driver'
postgresql_jdbc_path = 'lib/postgresql-42.3.4.jar'
postgresql_url = 'jdbc:postgresql://localhost:5432/'
postgresql_url_db = 'jdbc:postgresql://localhost:5432/db2'
postgresql_user = 'postgres'
postgresql_pw = 'PASSWORD'

init_conn = jdbc.connect(postgresql_class,
                         postgresql_url,
                         [postgresql_user, postgresql_pw],
                         postgresql_jdbc_path)

init_curs = init_conn.cursor()

# ReadFile
fileCreate = open("./schema/hr_create.sql", "r")
filePopulate = open("./schema/hr_populate.sql", "r")
fileComment = open("./schema/hr_comment.sql", "r")

# SQL
createDB = 'CREATE DATABASE db2'
createSchema = 'CREATE SCHEMA hr'
createTable = fileCreate.read()
populateTable = filePopulate.read()
createComment = fileComment.read()

# @TODO: implement go to db2

# create DB
try:
    init_curs.execute(createDB)
except:
    print("DB may exists already")

init_curs.close()
init_conn.close()

conn = jdbc.connect(postgresql_class,
                    postgresql_url_db,
                    [postgresql_user, postgresql_pw],
                    postgresql_jdbc_path)

curs = conn.cursor()

# create Schema
try:
    curs.execute(createSchema)
except:
    print("Schema may exists already")

# create Table
try:
    curs.execute(createTable)
except:
    print("Table may exists already")

# populate Table
try:
    curs.execute('SELECT * FROM hr.locations')
    if curs.fetchall() == []:
        curs.execute(populateTable)
    else:
        print("Table already filled")
except ValueError:
    print("Couldn't populate Table")

# comment Table
try:
    curs.execute(createComment)
except ValueError:
    print("Couldn't comment on Table")


#select Table
try:
    curs.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.locations) e;')
    return_value = curs.fetchall()
    #print(return_value)

    jsonFile = open("pg_fetch.json", "w")
    jsonFile.write("")
    jsonFile.close()


    for return_object in return_value:
        jsonFile = open("./storage/pg_fetch.json", "a")
        for row in return_object:
            #print(row)
            jsonFile.write(str(row))
        jsonFile.close()

except ValueError:
    print(ValueError)


# curs.execute('SELECT * FROM csv_reports LIMIT 2')
# curs.fetchall()
curs.close()
conn.close()
