from countryinfo import CountryInfo

count = input("País: ")
country = CountryInfo(count)
print("Capital é:", country.capital())
print("Moeda: ", country.currencies())
print("Linguagem: ", country.languages())
print("População: ", country.population())
print("Fronteiras: ", country.borders())
print("Outros nomes: ", country.alt_spellings())
