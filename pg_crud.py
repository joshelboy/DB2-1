import jaydebeapi as jdbc

# sql = 'Select * From world.city'
postgresql_class = 'org.postgresql.Driver'
postgresql_jdbc_path = 'lib/postgresql-42.3.4.jar'
postgresql_url_db = 'jdbc:postgresql://localhost:5432/db2'
postgresql_user = 'postgres'
postgresql_pw = 'LOTTI007'

conn = jdbc.connect(postgresql_class,
                    postgresql_url_db,
                    [postgresql_user, postgresql_pw],
                    postgresql_jdbc_path)

curs = conn.cursor()


def convert(table_choice_input, fetched_data):
    try:
        table_choice_input = int(table_choice_input)

        table_choice = fetched_data[table_choice_input - 1][1]
        return table_choice
    except:
        curs.execute("SELECT * FROM pg_catalog.pg_tables WHERE tablename = '" + table_choice_input + "'")
        return_value = curs.fetchall()
        if return_value != []:
            print("Found as string")
            return return_value[0][1]
        else:
            return "Unknown input. Please enter number or name next time."


def _create():
    curs.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'hr'")

    counter = 1
    fetched_data = curs.fetchall()
    for row in fetched_data:
        print(str(counter) + ".", row[1])
        counter = counter + 1

    table_choice_input = input("Auswahl: ")

    selected_table = convert(table_choice_input, fetched_data)

    curs.execute(
        "SELECT * FROM information_schema.columns WHERE table_schema = 'hr' AND table_name = '" + selected_table + "'")
    columns = curs.fetchall()

    l = []

    for row in columns:
        input_choice = input("Was wollen Sie zur Spalte '" + row[3] + "' hinzufügen?: ")
        l.append(input_choice)

    print(l)


def _read():
    return "read"


def _update():
    return "update"


def _delete():
    return "delete"
