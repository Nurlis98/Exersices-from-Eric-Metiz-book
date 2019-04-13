favorite_languages = {

    'Nile': 'Egypt',
    'Naryn': 'Kyrgyzstan',
    'Amazonka': 'South-America',

}

for name, language in favorite_languages.items():
    print(name.title() + " - through the " +
        language.title() + ".")

cityes = {
    'Paris': 'France',
    'Osh': 'Kyrgyzstan',
    'Berlin': 'Germany',
}

for city, other in cityes.items():
    print(city.title() + " - located in " +
        other.title() + ".")