cities = {
    'london': {
        'population': '8,136 mln',
        'location': 'Great Britain',
    },
    'bishkek': {
        'population': '933 753',
        'location': 'Kyrgyzstan',
    },
}
for city, city_info in cities.items():
    print("\nCity: " + city)
    full_name = city_info['population'] + " " + city_info
    location = city_info['location']
    print("\tpopulation: " + full_name.title())
    print("\tLocation: " + location.title())
