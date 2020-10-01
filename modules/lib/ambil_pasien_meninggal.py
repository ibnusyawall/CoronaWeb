from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataMeninggal = covid.getDeath(country=negara)
for data in dataMeninggal:
    print ("Negara: " + data["country"])        # Take the name of the country
    print ("Meninggal: " + str(data["deaths"])) # Taking corona data died
    print ("-" * 25)
