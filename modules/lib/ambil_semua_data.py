from covid19.main import COVID

covid = COVID()
covid.get()
semua = covid.all
for data in semua:
    # Retrieves all corona data
    print ("Negara: " + data["country"])
    print ("Aktif : " + str(data["active"]))
    print ("Meninggal: " + str(data["deaths"]))
    print ("Sembuh: " + str(data["recovered"]))
    print ("Terkonfirmasi: " + str(data["confirmed"]))
    print ("-" * 25)
