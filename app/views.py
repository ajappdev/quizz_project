# DJANGO DECLARATIONS
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.templatetags.static import static
from django.template.loader import render_to_string
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

# GENERAL DECLARATIONS
import pandas as pd
import os
from django.http import JsonResponse
import json
from datetime import date, datetime
from os import path
from shutil import move

# APP DECLARATIONS
import app.models as am
import app.forms as af
import app.m00_common as m00
import app.m01_question as m01

# DECLARING FONCTIONS


def register(request):
    register_form = af.RegisterForm()
    registration_errors = ""
    if request.method == "POST":
        register_form = af.RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()

            user_profile = am.UserProfile()
            user_profile.user = user
            user_profile.username = request.POST['username']
            user_profile.save()

            login(request, user)

            return redirect("/")
        else:
            registration_errors = register_form.errors

    template = 'registration/register.html'
    context = {
        "register_form": register_form,
        "registration_errors": registration_errors}
    return render(request, template, context)


def landing_page(request):
    template = 'blank.html'

    context = {}
    return render(request, template, context)


def admin_settings(request):
    template = 'administrator/settings.html'

    regions = am.Region.objects.all()
    categories = am.Category.objects.all()
    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()
    context = {
        "regions": regions,
        "categories": categories,
        "countries": countries,
        "sub_categories": sub_categories,
        }
    return render(request, template, context)


def add_question(request):

    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()

    template = 'administrator/add-update-question.html'
    context = {
        "countries": countries,
        "sub_categories": sub_categories,
        }
    return render(request, template, context)


def update_question(request, pk: int):
    template = 'administrator/update-question.html'
    question = am.Question.objects.get(id=pk)
    context = {"question": question}
    return render(request, template, context)


def bulk_upload_questions(request):

    template = 'administrator/bulk-upload-questions.html'
    context = {
        }
    return render(request, template, context)


def initial_settings_upload(request):
    
    am.Country.objects.filter(id__gte=0).delete()
    am.Region.objects.filter(id__gte=0).delete()

    am.SubCategory.objects.filter(id__gte=0).delete()
    am.Category.objects.filter(id__gte=0).delete()


    geo_category = am.Category()
    geo_category.name = "Physical Geo"
    geo_category.save()

    sub_categories = [
        "Airport",
        "Analogy",
        "Ancient City",
        "Archipelago",
        "Attractions",
        "Bay",
        "Border",
        "Bridge",
        "Cape",
        "Capital City",
        "Capital on Island",
        "Capital on Mountain",
        "Capital on Peninsula",
        "Capital on River",
        "Capital on Valley",
        "City",
        "City on River",
        "Current Events",
        "Dam",
        "Definition",
        "Desert",
        "Directions",
        "Discoverer",
        "Elevation",
        "Ethnic Group",
        "Exports",
        "Festival",
        "Former Capital",
        "Former Colony",
        "Former Name",
        "Fun Geo",
        "Geo Extreme",
        "Highest Point",
        "HP on Mountain",
        "Independence",
        "Island",
        "Largest City",
        "Largest Desert",
        "Largest Island",
        "Largest Lake",
        "Lowest Point",
        "Motto",
        "Mountain",
        "National Animal",
        "National Bird",
        "National Dish",
        "National Flag",
        "National Park",
        "Other Capital",
        "Peninsula",
        "Plateau",
        "Region",
        "Strait",
        "UNESCO",
        "War",
        "Water Body"]

    for sub_category in sub_categories:
        new_sub_category = am.SubCategory()
        new_sub_category.name = sub_category
        new_sub_category.category = geo_category
        new_sub_category.save()

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
        print(country)
        new_country = am.Country()
        new_country.name = country
        new_country.region = region_africa
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
        new_country.region = region_europe
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
        new_country.region = region_asia
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
        new_country.region = region_north_america
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
        new_country.region = region_north_america
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
        new_country.region = region_south_america
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
        new_country.region = region_australia
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
        new_country.region = region_carriban
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
        new_country.region = region_us
        new_country.save()
    template = 'administrator/initial-settings.html'
    context = {
        }
    return render(request, template, context)


def questions(request):
    template = 'administrator/questions.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Question was successfully created"
    elif success_message == "updated":
        success_message = "Question was successfully updated"
    else:
        success_message = ""

    regions = am.Region.objects.all()
    categories = am.Category.objects.all()
    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()

    questions = am.Question.objects.all()
    context = {
        "questions": questions,
        "success_message": success_message,
        "regions": regions,
        "categories": categories,
        "countries": countries,
        "sub_categories": sub_categories}

    return render(request, template, context)


@csrf_exempt
def upload_questions_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("0")

        for f in files:
            fs = FileSystemStorage(path.join(
                settings.MEDIA_ROOT))
            filename = fs.save(request.POST['key'] + ".xlsx", f)

        file_path = os.path.join(
            settings.MEDIA_ROOT, request.POST['key'] + ".xlsx")
        
        error_upload = m01.check_bulk_upload(file_path)
        if error_upload == "":
            treatment_result = m01.bulk_upload(file_path)
            html = render_to_string(
                template_name="administrator/widgets/bulk-treatment.html",
                context={
                    "treatment_result": treatment_result,
                }
            )
            data_dict = {"error": "", "html": html}
        else:
            print(error_upload)
            data_dict = {"error": error_upload} 

        return JsonResponse(data=data_dict, safe=False)


def ajax_calls(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        action = received_json_data['action']

        if action == "get_current_regions":
            current_regions = list(
                am.Region.objects.all().values("id", "name"))
            data_dict = {"current_regions": current_regions}

        elif action == "look_for_childs":
            if received_json_data['what'] == "countries":
                if received_json_data['parent'] == "":
                    childs = list(am.Country.objects.all().values("id", "name"))
                else:
                    childs = list(am.Country.objects.filter(
                        region=str(received_json_data['parent'])).values(
                            "id", "name"))
            elif received_json_data['what'] == "sub_categories":
                if received_json_data['parent'] == "":
                    childs = list(am.SubCategory.objects.all().values("id", "name"))
                else:
                    childs = list(am.SubCategory.objects.filter(
                        category=str(received_json_data['parent'])).values(
                            "id", "name"))

            data_dict = {"childs": childs}


        elif action == "save_question_form":

            error_message = ""
            question_type = ""
            if received_json_data['question_type'] == "freetext":
                question_type = "Free Text"
            elif received_json_data['question_type'] == "truefalse":
                question_type = "True or False"
            elif received_json_data['question_type'] == "multiplechoices":
                question_type = "Multiple Choices"
            else:
                question_type = received_json_data['question_type']

            try: 
                error_message = m01.create_question(
                    question_type,
                    received_json_data['question_choices'],
                    received_json_data['question_answer'],
                    received_json_data['question_country'],
                    received_json_data['question_text'],
                    received_json_data['question_sub_category'],
                )
            except Exception as e:
                error_message = e

            data_dict = {"error_message": str(error_message)}

        elif action == "get_current_categories":
            current_categories = list(
                am.Category.objects.all().values("id", "name"))
            data_dict = {"current_categories": current_categories}

        elif action == "add_country":
            error = 0
            error_text = ""
            new_country_id = 0

            if received_json_data['country_name'] != "":
                try:
                    new_country = am.Country()
                    new_country.name=received_json_data['country_name']
                    new_country.region=am.Region.objects.get(
                        id=int(received_json_data['region_id']))
                    new_country.save()
                    new_country_id = new_country.id
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, ADD_COUNTRY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Country name cannot be empty!"
                error = 1
            data_dict = {
                "error": error,
                "error_text": error_text,
                "new_country_id": new_country_id}

        elif action == "delete_country":
            error = 0
            error_text = ""
            try:
                am.Country.objects.filter(
                    id=int(received_json_data['country_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_COUNTRY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "update_country":
            error = 0
            error_text = ""
            if received_json_data['country_name'] != "":
                try:
                    am.Country.objects.filter(
                        id=int(received_json_data['country_id'])).update(
                            name=received_json_data['country_name'],
                            region=am.Region.objects.get(
                                id=int(received_json_data['country_region'])))
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_COUNTRY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Country name cannot be empty!"
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "add_sub_category":
            error = 0
            error_text = ""
            new_sub_category_id = 0
            if received_json_data['sub_category_name'] != "":
                try:
                    new_sub_category = am.SubCategory()
                    new_sub_category.name=received_json_data['sub_category_name']
                    new_sub_category.category=am.Category.objects.get(
                        id=int(received_json_data['parent_category_id']))
                    new_sub_category.save()
                    new_sub_category_id = new_sub_category.id
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, ADD_SUB_CATEGORY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Sub category name cannot be empty!"
                error = 1
            data_dict = {
                "error": error,
                "error_text": error_text,
                "new_sub_category_id": new_sub_category_id}

        elif action == "delete_sub_category":
            error = 0
            error_text = ""
            try:
                am.SubCategory.objects.filter(
                    id=int(received_json_data['sub_category_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_SUB_CATEGORY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "update_sub_category":
            error = 0
            error_text = ""
            if received_json_data['sub_category_name'] != "":
                try:
                    am.SubCategory.objects.filter(
                        id=int(received_json_data['sub_category_id'])).update(
                            name=received_json_data['sub_category_name'],
                            category=am.Category.objects.get(
                                id=int(received_json_data['sub_category_parent_category'])))
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_SUB_CATEGORY, 1, " + str(e)
                    error = 1
                data_dict = {"error": error, "error_text": error_text}
            else:
                error_text = "Sub category name cannot be empty!"
                error = 1
        elif action == "add_region":
            error = 0
            error_text = ""
            new_region_id = 0
            if received_json_data['region_name'] != "":
                try:
                    new_region = am.Region()
                    new_region.name=received_json_data['region_name']
                    new_region.save()
                    new_region_id = new_region.id
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, ADD_REGION, 1, " + str(e)
                    error = 1
            else:
                error_text = "Region name cannot be empty!"
                error = 1
            data_dict = {
                "error": error,
                "error_text": error_text,
                "new_region_id": new_region_id}

        elif action == "delete_question":
            error = 0
            error_text = ""
            try:
                am.Question.objects.filter(
                    id=int(received_json_data['question_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_QUESTION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "delete_region":
            error = 0
            error_text = ""
            try:
                am.Region.objects.filter(
                    id=int(received_json_data['region_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_REGION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "update_region":
            error = 0
            error_text = ""
            if received_json_data['region_name'] != "":
                try:
                    am.Region.objects.filter(
                        id=int(received_json_data['region_id'])).update(
                            name=received_json_data['region_name'])
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_REGION, 1, " + str(e)
                    error = 1
            else:
                error_text = "Region name cannot be empty!"
                error = 1

            data_dict = {"error": error, "error_text": error_text}

        elif action == "add_category":
            error = 0
            error_text = ""
            new_category_id = 0
            if received_json_data['category_name'] != "":
                try:
                    new_category = am.Category()
                    new_category.name=received_json_data['category_name']
                    new_category.save()
                    new_category_id = new_category.id
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, ADD_CATEGORY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Category name cannot be empty!"
                error = 1

            data_dict = {
                "error": error,
                "error_text": error_text,
                "new_category_id": new_category_id}

        elif action == "delete_category":
            error = 0
            error_text = ""
            try:
                am.Category.objects.filter(
                    id=int(received_json_data['category_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_CATEGORY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "update_category":
            error = 0
            error_text = ""
            if received_json_data['category_name'] != "":
                try:
                    am.Category.objects.filter(
                        id=int(received_json_data['category_id'])).update(
                            name=received_json_data['category_name'])
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_CATEGORY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Category name cannot be empty!"
                error = 1

            data_dict = {"error": error, "error_text": error_text}

        if action == "filter_questions_list":
    
            question_keyword = received_json_data['question_keyword']
            question_type = received_json_data['question_type']
            page = received_json_data['page']

            questions = am.Question.objects.filter(
                question__icontains=question_keyword,
                type__icontains=question_type
            )

            try:
                questions = questions.filter(
                    country__id=int(received_json_data['question_country']))
            except Exception as e:
                pass

            try:
                questions = questions.select_related("country").filter(
                    country__region__id=int(
                        received_json_data['question_region']))
            except Exception as e:
                pass

            try:
                questions = questions.filter(
                    sub_category__id=int(
                        received_json_data['question_sub_category']))
            except Exception as e:
                pass

            try:
                questions = questions.select_related("sub_category").filter(
                    sub_category__category__id=int(
                        received_json_data['question_category']))
            except Exception as e:
                pass



            questions_list = m00.pagination(page, 10, questions)

            html = render_to_string(
                        template_name="administrator/questions-table.html", 
                        context={
                            "questions": questions_list,
                        }
                    )
            data_dict = {"html": html}


        return JsonResponse(data=data_dict, safe=False)