
from datetime import datetime

# Declaring django modules
from django.core.paginator import Paginator

# Declaring app models
import app.models as am

# Declaring Global Variables

DATE_SHORT_LOCAL_WITH_DASH: str = '%Y-%m-%d'

def pagination(page: int, nbr_pag: int, liste_obj):
    paginator = Paginator(liste_obj, nbr_pag)
    obj = paginator.get_page(page)
    return obj

def initial_settings():
    #CLEAN THE BASE
    am.Country.objects.filter(id__gte=0).delete()
    am.Region.objects.filter(id__gte=0).delete()

    am.SubCategory.objects.filter(id__gte=0).delete()
    am.Category.objects.filter(id__gte=0).delete()


    #SAVE CATEGORIES AND SUB CATEGORIES

    ####################################################
    ####################################################
    new_category = am.Category()
    new_category.name = "CE Geo"
    new_category.save()

    sub_categories = [
        'Cultural Geo',
        'Current Events',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()

        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Comparison Geo"
    new_category.save()

    sub_categories = [
            'Analogy',
            'Area',
            'Attractions',
            'Border',
            'Capital City',
            'City',
            'Coastline',
            'Comparison',
            'Definition',
            'Desert',
            'Direction',
            'Directions',
            'Elevation',
            'Ethnic Group',
            'Exports',
            'Former Colony',
            'GDP',
            'Geo Extreme',
            'Height',
            'Highest Point',
            'Independence',
            'Island',
            'Kingdom',
            'Language',
            'Location',
            'Longitude',
            'Mountain',
            'National Flag',
            'National Park',
            'Odd Item Out',
            'Peninsula',
            'Population',
            'Rainforest',
            'Region',
            'Religion',
            'River Borders',
            'Rivers',
            'School Bee',
            'Size',
            'State Bee',
            'Three Clues',
            'Timezone',
            'Tropics',
            'True Or False',
            'War',
            'Water Body',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Cultural Geo"
    new_category.save()

    sub_categories = [
            'Airport',
            'Attractions',
            'Capital City',
            'City',
            'City on River',
            'Coat of Arms',
            'Comparison',
            'Currency',
            'Discoverer',
            'Ethnic Group',
            'Export',
            'Festival',
            'First Country',
            'Former Island',
            'Former Name',
            'Fun Geo',
            'Geo Extreme',
            'Headquarters',
            'Language',
            'Languages',
            'Largest City',
            'Motto',
            'Museum',
            'Music',
            'National Animal',
            'National Anthem',
            'National Bird',
            'National Dish',
            'National Flag',
            'National Flower',
            'National Forest',
            'National Monument',
            'National Park',
            'National Sport',
            'National Symbol',
            'Nickname',
            'Olympics',
            'Only Country',
            'Only State',
            'Others',
            'Religion',
            'Rivers',
            'School Bee',
            'Sport',
            'Sports',
            'State Bee',
            'Time Zone',
            'Timezone',
            'Tradition',
            'UNESCO',
            'Unusual Geo',
            'Unusual Name',
            'Valley',
            'Weird but True!',
            'What Four',
            'What Two'
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Economic Geo"
    new_category.save()

    sub_categories = [
            'Airport',
            'Attractions',
            'Border',
            'City',
            'Comparison',
            'Currency',
            'Dam',
            'Export',
            'Exports',
            'First Country',
            'Fun Geo',
            'GDP',
            'Geo Extreme',
            'Headquarters',
            'Landmark',
            'Largest City',
            'Motto',
            'National Bird',
            'National Flag',
            'National Park',
            'Nickname',
            'Numerical Geo',
            'Odd Item Out',
            'Only Country',
            'Others',
            'Population',
            'Port City',
            'Producer',
            'Region',
            'Rivers',
            'School Bee',
            'Space',
            'State Bee',
            'Tower',
            'Valley',
            'What Two',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Fun Geo"
    new_category.save()

    sub_categories = [
            'Unusual Name',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Historical Geo"
    new_category.save()

    sub_categories = [
        'Airport',
        'Ancient City',
        'Attractions',
        'Border',
        'Capital City',
        'City',
        'City on River',
        'Civilization',
        'Colony',
        'Comparison',
        'Definition',
        'Discoverer',
        'Empire',
        'Ethnic Group',
        'Explorer',
        'Exports',
        'Former Capital',
        'Former Colony',
        'Former Name',
        'Fun Geo',
        'Geo Extreme',
        'Independence',
        'Invention',
        'Island',
        'Kingdom',
        'Language',
        'Largest City',
        'Law',
        'Leader',
        'National Flag',
        'National Forest',
        'National Monument',
        'National Park',
        'Natural Disaster',
        'Nickname',
        'Ocean',
        'Odd Item Out',
        'Only Country',
        'Origin',
        'Others',
        'Politics',
        'Population',
        'President',
        'Region',
        'Religion',
        'Rivers',
        'Roman',
        'Ruler',
        'School Bee',
        'State Bee',
        'Treaty',
        'UNESCO',
        'Unusual Name',
        'War',
        'Water Body',
        'What Two',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Human Geo"
    new_category.save()

    sub_categories = [
        'City',
        'City on River',
        'Comparison',
        'Ethnic Group',
        'Geo Extreme',
        'Lake',
        'Largest City',
        'Most Populous',
        'Population',
        'School Bee',
        'State Bee',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Nationals"
    new_category.save()

    sub_categories = [
        'Peninsula',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Numerical Geo"
    new_category.save()

    sub_categories = [
        'Attractions',
        'Border',
        'Capital City',
        'Capital on River',
        'City',
        'Comparison',
        'Currency',
        'Definition',
        'Desert',
        'Directions',
        'Discoverer',
        'Former Colony',
        'Fun Geo',
        'Geo Extreme',
        'Independence',
        'Island',
        'Language',
        'Law',
        'National Flag',
        'Numbers',
        'Numerical Geo',
        'Peninsula',
        'Population',
        'Region',
        'Rivers',
        'School Bee',
        'Sports',
        'State Bee',
        'Time Zone',
        'UNESCO',
        'Unusual Name',
        'Water Body',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Others"
    new_category.save()

    sub_categories = [
        'Analogy',
        'Comparison',
        'Others',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Political Geo"
    new_category.save()

    sub_categories = [
        'Bay',
        'Border',
        'Borders',
        'Capital City',
        'Capital on Island',
        'Capital on Lake',
        'Capital on Mountain',
        'Capital on Peninsula',
        'Capital on River',
        'Capital on Water Body',
        'City',
        'City on Bay',
        'City on Island',
        'City on Lake',
        'City on River',
        'City on Water Body',
        'Comparison',
        'Confluence of River',
        'Country Border',
        'Country Borders',
        'Definition',
        'Department',
        'Exclave',
        'Former Capital',
        'Former Name',
        'Fun Geo',
        'Geo Extreme',
        'HP on Mountain',
        'HQ',
        'Island',
        'Lake',
        'Largest City',
        'Longest River',
        'Mountain',
        'National',
        'National Grassland',
        'Nickname',
        'Odd Item Out',
        'Only Country',
        'Only State',
        'Other Capital',
        'Populous',
        'Port City',
        'Provinces',
        'Region',
        'River',
        'River Borders',
        'Rivers',
        'School Bee',
        'State Bee',
        'State Border',
        'State Borders',
        'Territory',
        'Three Clues',
        'Tributary',
        'Unusual Name',
        'Water Body',
        'Waterbody',
        'Weird but True!',
        'What Three',
        'What Two',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()

    ####################################################
    ####################################################

    new_category = am.Category()
    new_category.name = "Physical Geo"
    new_category.save()

    sub_categories = [
        'Airport',
        'Analogy',
        'Archipelago',
        'Area',
        'Bay',
        'Border',
        'Borders',
        'Cape',
        'Capital City',
        'Capital on Mountain',
        'Capital on River',
        'Capital on Valley',
        'City',
        'City on Island',
        'City on River',
        'Coastline',
        'Comparison',
        'Confluence',
        'Confluence of River',
        'Country Border',
        'Country Borders',
        'Dam',
        'Definition',
        'Desert',
        'Dispute',
        'Ethnic Group',
        'Festival',
        'Fjord',
        'Former Name',
        'Fun Geo',
        'Geo Extreme',
        'Glacier',
        'Gulf',
        'Highest Mountain',
        'Highest Point',
        'HP Old Name',
        'HP on Desert',
        'HP on Island',
        'HP on Mountain',
        'HP on National Park',
        'HP on NP',
        'HP on Plateau',
        'Isand',
        'Island',
        'Islands',
        'Lake',
        'Lake in 2 States',
        'Lakes',
        'Landforms',
        'Largest',
        'Largest City',
        'Largest Island',
        'Largest Lake',
        'Largest River',
        'Longest River',
        'Lowest Point',
        'Motto',
        'Mountain',
        'Name',
        'Natiional Park',
        'National Forest',
        'National Monument',
        'National Park',
        'National Park on Island',
        'National Park on Lake',
        'National Park on River',
        'National Preserve',
        'National Seashore',
        'National Wildlife',
        'Nationals Bee',
        'Natonal Monument',
        'Nickname',
        'Ocean',
        'Odd Item Out',
        'Only Country',
        'Only Place',
        'Only State',
        'Other Capital',
        'Others',
        'Peninsula',
        'Plateau',
        'Port City',
        'Region',
        'Regions',
        'Reservoir',
        'River Separation',
        'Rivers',
        'School Bee',
        'Smallest Island',
        'Sound',
        'State Bee',
        'State Border',
        'State Borders',
        'Strait',
        'Term',
        'Three Clues',
        'Tributary',
        'Tropics',
        'UNESCO',
        'Unusual Name',
        'Valley',
        'Volcano',
        'Water Body',
        'Weird but True!',
        'What Four',
        'What Three',
        'What Two',
        ]

    for sub_category in sub_categories:
        if len(am.SubCategory.objects.filter(name=sub_category)) > 0:
            new_sub_category = am.SubCategory.objects.filter(name=sub_category)[0]
        else:
            new_sub_category = am.SubCategory()
            new_sub_category.name = sub_category
            new_sub_category.save()
            
        new_sub_category.category.add(new_category)
        new_sub_category.save()


    #SAVE COUNTRIES
    region_africa = am.Region()
    region_africa.name = "Africa"
    region_africa.save()

    africa_countries = ["Algeria",
    "Angola",
    "Benin",
    "Botswana",
    "Burkina",
    "Burundi",
    "Cameroon",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Comoros",
    "Congo",
    "Democratic Republic of Congo",
    "Djibouti",
    "Egypt",
    "Equatorial Guinea",
    "Eritrea",
    "Ethiopia",
    "Gabon",
    "Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
    "Ivory Coast",
    "Kenya",
    "Lesotho",
    "Liberia",
    "Libya",
    "Madagascar",
    "Malawi",
    "Mali",
    "Mauritania",
    "Mauritius",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Niger",
    "Nigeria",
    "Rwanda",
    "Sao Tome and Principe",
    "Senegal",
    "Seychelles",
    "Sierra Leone",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Sudan",
    "Swaziland",
    "Tanzania",
    "Togo",
    "Tunisia",
    "Uganda",
    "Zambia",
    "Zimbabwe"]

    for country in africa_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_africa)
        new_country.save()

    region_europe = am.Region()
    region_europe.name = "Europe"
    region_europe.save()

    europe_countries = [
        "Albania",
        "Andorra",
        "Armenia",
        "Austria",
        "Azerbaijan",
        "Belarus",
        "Belgium",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Georgia",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Ireland",
        "Italy",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macedonia",
        "Malta",
        "Moldova",
        "Monaco",
        "Montenegro",
        "Netherlands",
        "Norway",
        "Poland",
        "Portugal",
        "Romania",
        "Russia",
        "San Marino",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Ukraine",
        "United Kingdom",
        "Vatican City"
    ]   

    for country in europe_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_europe)
        new_country.save()

    region_asia = am.Region()
    region_asia.name = "Asia"
    region_asia.save()

    asia_countries = [
        "Afghanistan",
        "Bahrain",
        "Bangladesh",
        "Bhutan",
        "Brunei",
        "Myanmar",
        "Cambodia",
        "China",
        "East Timor",
        "Indonesia",
        "Iran",
        "Iraq",
        "Israel",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "North Korea",
        "South Korea",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Lebanon",
        "Malaysia",
        "Maldives",
        "Mongolia",
        "Nepal",
        "Oman",
        "Pakistan",
        "Philippines",
        "Qatar",
        "Russia",
        "Saudi Arabia",
        "Singapore",
        "Sri Lanka",
        "Syria",
        "Tajikistan",
        "Thailand",
        "Turkey",
        "Turkmenistan",
        "United Arab Emirates",
        "Uzbekistan",
        "Vietnam",
        "Yemen",
        "India"
    ]   

    for country in asia_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_asia)
        new_country.save()

    region_north_america = am.Region()
    region_north_america.name = "North America"
    region_north_america.save()

    norh_america_countries = [
        "Belize",
        "Canada",
        "Costa Rica",
        "El Salvador",
        "Grenada",
        "Guatemala",
        "Honduras",
        "Mexico",
        "Nicaragua",
        "Panama"
    ]   

    for country in norh_america_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_north_america)
        new_country.save()

    region_south_america = am.Region()
    region_south_america.name = "South America"
    region_south_america.save()

    south_america_countries = [
        "Argentina",
        "Bolivia",
        "Brazil",
        "Chile",
        "Colombia",
        "Ecuador",
        "Guyana",
        "Paraguay",
        "Peru",
        "Suriname",
        "Uruguay",
        "Venezuela"
    ]   

    for country in south_america_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_south_america)
        new_country.save()

    region_australia = am.Region()
    region_australia.name = "Australia"
    region_australia.save()

    australia_countries = [
        "Fiji",
        "Kiribati",
        "Marshall Islands",
        "Micronesia",
        "Nauru",
        "New Zealand",
        "Palau",
        "Papua New Guinea",
        "Samoa",
        "Solomon Islands",
        "Tonga",
        "Tuvalu",
        "Vanuatu",
        "Australia"
    ]   

    for country in australia_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_australia)
        new_country.save()


    region_carriban = am.Region()
    region_carriban.name = "Caribbean"
    region_carriban.save()

    carriban_countries = [
        "Cuba",
        "Haiti",
        "Dominican Republic",
        "Antigua and Barbuda",
        "Jamaica",
        "Trinidad and Tobago",
        "Bahamas",
        "Barbados",
        "Saint Lucia",
        "Saint Vincent and the Grenadines",
        "Dominica",
        "Grenada",
        "Saint Kitts and Nevis"
    ]   

    for country in carriban_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_carriban)
        new_country.save()


    region_us = am.Region()
    region_us.name = "United states"
    region_us.save()

    us_countries = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
        "Guam",
        "American Samoa",
        "Northern Mariana Islands",
        "Puerto Rico",
        "US Virgin Islands"
    ]   

    for country in us_countries:
        new_country = am.Country()
        new_country.name = country
        new_country.save()
        new_country.region.add(region_us)
        new_country.save()