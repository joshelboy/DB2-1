import MongoDB
import Redis
import PostgreSQL

def _create():
    if auswahlCRUD == str(1):
        PostgreSQL._create()
    elif auswahlCRUD == str(2):
        Redis._create()
    elif auswahlCRUD == str(3):
        MongoDB._create()

def _read():
    if auswahlCRUD == str(1):
        PostgreSQL._read()
    elif auswahlCRUD == str(2):
        Redis._read()
    elif auswahlCRUD == str(3):
        MongoDB._read()

def _update():
    if auswahlCRUD == str(1):
        PostgreSQL._update()
    elif auswahlCRUD == str(2):
        Redis._update()
    elif auswahlCRUD == str(3):
        MongoDB._update()

def _delete():
    if auswahlCRUD == str(1):
        PostgreSQL._delete()
    elif auswahlCRUD == str(2):
        Redis._delete()
    elif auswahlCRUD == str(3):
        MongoDB._delete()

askfordbs = True
auswahlDBS = ""
auswahlCRUD= ""

while(True):
    if(askfordbs):
        print("Zur Auswahl stehen:")
        print("1: Relationales Datenbanksystem (PostgreSQL)")
        print("2: Key-Value-System (Redis)")
        print("3: Dokumentenspeicher (MongoDB)")

        auswahlDBS = input("Gewähltes DBS: ")
        askfordbs = False

    print("Gewähltes DBS: ")
    print("Zur Auswahl stehen:")
    print("1: Create")
    print("2: Read")
    print("3: Update")
    print("4: Delete")
    print("5: Anderes DBS")

    auswahlCRUD = input("Auswahl: ")

    if auswahlCRUD == str(1):
        _create()
    elif auswahlCRUD == str(2):
        _read()
    elif auswahlCRUD == str(3):
        _update()
    elif auswahlCRUD == str(4):
        _delete()
    elif auswahlCRUD == str(5):
        askfordbs = True