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

    regions = am.Region.objects.all()
    categories = am.Category.objects.all()
    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()

    template = 'administrator/add-update-question.html'
    context = {
        "regions": regions,
        "categories": categories,
        "countries": countries,
        "sub_categories": sub_categories,
        }
    return render(request, template, context)


def update_question(request, pk: int):
    template = 'administrator/update-question.html'
    question = am.Question.objects.get(id=pk)
    context = {"question": question}
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

    questions = am.Question.objects.all()
    context = {"questions": questions, "success_message": success_message}
    return render(request, template, context)


@csrf_exempt
def upload_id_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("0")

        for f in files:
            fs = FileSystemStorage(path.join(
                settings.MEDIA_ROOT))
            filename = fs.save(request.POST['key'] + ".jpg", f)
        try:
            file_path = os.path.join(
                settings.MEDIA_ROOT, request.POST['key'] + ".jpg")
            if request.POST['key'] == "PASSPORT":
                result = m00.process_id_card(file_path)
            else:
                result = m00.process_passport(file_path)
            data_dict = {"MRZ_found": 1, "id_reading": result, "tmp_file": request.POST['key'] + ".jpg"}
        except Exception as e:
            print(e)
            data_dict = {"MRZ_found": 0, "tmp_file": request.POST['key'] + ".jpg"}

        return JsonResponse(data=data_dict, safe=False)


def ajax_calls(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        action = received_json_data['action']

        if action == "get_current_regions":
            current_regions = list(
                am.Region.objects.all().values("id", "name"))
            data_dict = {"current_regions": current_regions}

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

        if action == "filter_customers_list":

            customer_name_or_id = received_json_data['customer_name_or_id']
            customer_nationality = received_json_data['customer_nationality']
            customer_type = received_json_data['customer_type']
            page = received_json_data['page']
    
            customers = am.Customer.objects.filter(
                Q(complete_name__icontains=customer_name_or_id) |
                Q(identity_number__icontains=customer_name_or_id),
                nationality__icontains=customer_nationality
            )

            customers = [
                c for c in customers if customer_type in c.type_customer()]

            customers_list = m00.pagination(page, 10, customers)

            html = render_to_string(
                        template_name="customer/customers-table.html", 
                        context={
                            "customers": customers_list,
                        }
                    )
            data_dict = {"html": html}


        return JsonResponse(data=data_dict, safe=False)