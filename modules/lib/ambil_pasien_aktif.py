from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataAktif = covid.getActive(country=negara)
for data in dataAktif:
    print ("Negara: " + data["country"])     # Take the name of the country
    print ("Aktif : " + str(data["active"])) # Retrieves active corona data
    print ("-" * 25)
