from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
terkonfirmasi = covid.getConfirmed(country=negara)
for data in terkonfirmasi:
    print ("Negara: " + data["country"])               # Take the name of the country
    print ("Terkonfirmasi: " + str(data["confirmed"])) # Retrieving confirmed data
    print ("-" * 25)
