from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataMeninggal = covid.getRecov(country=negara)
for data in dataMeninggal:
    print ("Negara: " + data["country"])        # Take the name of the country
    print ("Sembuh: " + str(data["recovered"])) # Retrieving recovered corona data
    print ("-" * 25)
