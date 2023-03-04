
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
        'Others'
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

    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Others"
    new_region.save()

    countries = [
        'Others'
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()

    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Africa"
    new_region.save()

    countries = [
        'Algeria',
        'Angola',
        'Benin',
        'Botswana',
        'Burkina Faso',
        'Burundi',
        'Cameroon',
        'Cape Verde',
        'Central African Republic',
        'Chad',
        'Comoros',
        "Cote d'Ivoire",
        'Democratic Republic of the Congo',
        'Djibouti',
        'Ecuador',
        'Egypt',
        'Equatorial Guinea',
        'Eritrea',
        'eSwatini',
        'Ethiopia',
        'Gabon',
        'Gambia',
        'Ghana',
        'Guinea',
        'Guinea Bissau',
        'Kenya',
        'Lebanon',
        'Lesotho',
        'Liberia',
        'Libya',
        'Madagascar',
        'Madagaskar',
        'Malawi',
        'Mali',
        'Mauritania',
        'Mauritius',
        'MB32',
        'Mongolia',
        'Morocco',
        'Morocco ',
        'Mozambique',
        'Namibia',
        'Niger',
        'Nigeria',
        'Republic of the Congo',
        'Rwanda',
        'Rwanda',
        'Sao Tome and Principe',
        'São Tomé and Príncipe',
        'Senegal',
        'Seychelles',
        'Sierra Leone',
        'Somalia',
        'South Africa',
        'South Sudan',
        'Sudan',
        'Syria',
        'Tanzania',
        'Togo',
        'Tonga',
        'Tunisia',
        'U.K.',
        'Uganda',
        'Western Sahara',
        'Yemen',
        'Zambia',
        'Zimbabwe',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Antarctica"
    new_region.save()

    countries = [
        'Antarctica',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()

    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Asia"
    new_region.save()

    countries = [
        'Afghanistan',
        'Armenia',
        'Asia',
        'Azerbaijan',
        'Bahrain',
        'Bangladesh',
        'Bhutan',
        'Brunei',
        'Cambodia',
        'China',
        'Cyprus',
        'East Timor',
        'Egypt',
        'Fiji',
        'France',
        'Georgia',
        'Ghana',
        'Greece',
        'Hong Kong',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ireland',
        'Israel',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Kazakhstan  ',
        'Khazakhstan',
        'Korean',
        'Kuwait',
        'Kyrgyzstan',
        'Kyrgzstan',
        'Laos',
        'Lebanon',
        'Macau',
        'Malaysia',
        'Maldives',
        'Mauritius',
        'Mongolia',
        'Mozambique',
        'Myanmar',
        'Nepal',
        'North Korea',
        'Oman',
        'Pakistan',
        'Palestine',
        'Papa New Guinea',
        'Papua New Guinea',
        'Philippines',
        'Phillippines',
        'Qatar',
        'Russia',
        'Saudi Arabia',
        'Seychelles',
        'Singapore',
        'South Korea',
        'Sri Lanka',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Thailand',
        'Timor Leste',
        'Timor-Leste',
        'Turkey',
        'Turkmenistan',
        'U.S.',
        'UAE',
        'United Arab Emirates',
        'Uzbekistan',
        'Vietnam',
        'Yemen',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Australia"
    new_region.save()

    countries = [
        'Australia',
        'Federated States of Micronesia',
        'France',
        'Marshall Islands',
        'Micronesia',
        'Nauru',
        'New Zealand',
        'Palau',
        'Papua New Guinea',
        'Samoa',
        'Solomon Islands',
        'Tonga',
        'Tuvalu',
        'Vanuatu',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Carribean"
    new_region.save()

    countries = [
        'Antigua and Barbuda',
        'Bahamas',
        'Barbados',
        'Cuba',
        'Dominica',
        'Dominican Republic',
        'Grenada',
        'Guyana',
        'Haiti',
        'Jamaica',
        'São Tomé and Príncipe',
        'St Kitts and Nevis',
        'St. Kitts and Nevis',
        'St. Vincent and Grenadines',
        'St. Vincent and the Grenadines',
        'St.Kitts and Nevis',
        'St.Lucia',
        'St.Vincent and Grenadines',
        'St.Vincent and the Grenadines',
        'Trinidad and Tobago',
        'Venezuela',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "China"
    new_region.save()

    countries = [
        'Mongolia',
        'Philippines',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Oceania"
    new_region.save()

    countries = [
        'Australia',
        'Federated States of Micronesia',
        'Fiji',
        'Kiribati',
        'Marshall Islands',
        'Nauru',
        'New Zealand',
        'Palau',
        'Papua New Guinea',
        'Samoa',
        'Tahiti',
        'Timor-Leste',
        'Tonga',
        'Tuvalu',
        'U.S.',
        'Vanuatu',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()

    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "South America"
    new_region.save()

    countries = [
        'Argentina',
        'Bolivia',
        'Brazil',
        'Chile',
        'Colombia',
        'Ecuador',
        'Ecudaor',
        'France',
        'Guatemala',
        'Guyana',
        'Panama',
        'Paraguay',
        'Peru',
        'Suriname',
        'Uruguay',
        'Venezuela',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Territory"
    new_region.save()

    countries = [
        'Denmark',
        'France',
        'Netherlands',
        'New Zealand',
        'Spain',
        'U.K.',
        'U.S.',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "North America"
    new_region.save()

    countries = [
        'Bahamas',
        'Barbados',
        'Belize',
        'Bermuda',
        'Canada',
        'Colombia',
        'Costa Rica',
        'Cuba',
        'Dominica',
        'Dominican Republic',
        'El Salvador',
        'France',
        'Greenland',
        'Grenada',
        'Guam',
        'Guatemala',
        'Haiti',
        'Honduras',
        'Idaho',
        'Jamaica',
        'Marshall Islands',
        'Maryland',
        'Mexico',
        'Michigan',
        'Netherlands',
        'Nevada',
        'New Jersey',
        'New York',
        'Nicaragua',
        'Northern Mariana Islands',
        'Panama',
        'Solentiname Islands',
        'South Dakota',
        'Texas',
        'Trinidad & Tobago',
        'Trinidad and Tobago',
        'Trinidad and Tobago ',
        'U.S.',
        'Virginia',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()


    ####################################################
    ####################################################

    new_region = am.Region()
    new_region.name = "Europe"
    new_region.save()

    countries = [
        'Albania',
        'Andorra',
        'Austria',
        'Belarus',
        'Belgium',
        'Bosnia and Herzegovina',
        'Brazil',
        'Bulgaria',
        'Croatia',
        'Czech Republic',
        'Denmark',
        'Estonia',
        'Finland',
        'France',
        'Georgia',
        'Germany',
        'Greece',
        'Greenland',
        'Hungary',
        'Iceland',
        'Ireland',
        'Italy',
        'Kosovo',
        'Latvia',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Malta',
        'Moldova',
        'Monaco',
        'Montenegro',
        'Morocco',
        'Netherlands',
        'Nort Macedonia',
        'North Macedonia',
        'Norway',
        'Poland',
        'Portugal',
        'Romania',
        'Russia',
        'San Marino',
        'Scotland',
        'Serbia',
        'Sisak',
        'Slovakia',
        'Slovenia',
        'Spain',
        'Split',
        'Sweden',
        'Switzerland',
        'Tajikistan',
        'Tanzania',
        'The Kornati Islands or  Stomorski Islands',
        'Turkey',
        'U.K.',
        'Ukraine',
        'United Kingdom',
        'Vatican City',
        'Wales',
        'Zadar',
        ]

    for country in countries:
        if len(am.Country.objects.filter(name=country)) > 0:
            new_country = am.Country.objects.filter(name=country)[0]
        else:
            new_country = am.Country()
            new_country.name = country
            new_country.save()
            
        new_country.region.add(new_region)
        new_country.save()