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


def add_question(request):
    template = 'administrator/add-question.html'
    context = {}
    return render(request, template, context)


def add_region(request):
    template = 'administrator/add-region.html'
    context = {}
    return render(request, template, context)


def add_country(request):
    template = 'administrator/add-country.html'
    context = {}
    return render(request, template, context)


def add_category(request):
    template = 'administrator/add-category.html'
    context = {}
    return render(request, template, context)


def add_sub_category(request):
    template = 'administrator/add-subcategory.html'
    context = {}
    return render(request, template, context)


def update_country(request, pk: int):
    template = 'administrator/update-country.html'
    country = am.Country.objects.get(id=pk)
    context = {"country": country}
    return render(request, template, context)


def update_region(request, pk: int):
    template = 'administrator/update-region.html'
    region = am.Region.objects.get(id=pk)
    context = {"region": region}
    return render(request, template, context)


def update_category(request, pk: int):
    template = 'administrator/update-category.html'
    category = am.Category.objects.get(id=pk)
    context = {"category": category}
    return render(request, template, context)


def update_sub_category(request, pk: int):
    template = 'administrator/update-subcategory.html'
    sub_category = am.SubCategory.objects.get(id=pk)
    context = {"sub_category": sub_category}
    return render(request, template, context)


def update_question(request, pk: int):
    template = 'administrator/update-question.html'
    question = am.Question.objects.get(id=pk)
    context = {"question": question}
    return render(request, template, context)


def questions(request):
    template = 'questions/index.html'

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


def countries(request):
    template = 'administrator/countries.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Country was successfully created"
    elif success_message == "updated":
        success_message = "Country was successfully updated"
    else:
        success_message = ""

    countries = am.Country.objects.all()
    context = {"countries": countries, "success_message": success_message}
    return render(request, template, context)


def regions(request):
    template = 'administrator/regions.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Region was successfully created"
    elif success_message == "updated":
        success_message = "Region was successfully updated"
    else:
        success_message = ""

    regions = am.Region.objects.all()
    context = {"regions": regions, "success_message": success_message}
    return render(request, template, context)


def categories(request):
    template = 'administrator/categories.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Category was successfully created"
    elif success_message == "updated":
        success_message = "Category was successfully updated"
    else:
        success_message = ""

    categories = am.Category.objects.all()
    context = {"categories": categories, "success_message": success_message}
    return render(request, template, context)


def sub_categories(request):
    template = 'administrator/sub-categories.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Sub category was successfully created"
    elif success_message == "updated":
        success_message = "Sub category was successfully updated"
    else:
        success_message = ""

    sub_categories = am.SubCategory.objects.all()
    context = {"sub_categories": sub_categories, "success_message": success_message}
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


        if action == "filter_transactions_list":

            customer_name_or_id = received_json_data['customer_name_or_id']
            transaction_type = received_json_data['transaction_type']
            transaction_date = received_json_data['transaction_date']
            transaction_before = datetime.strptime(
                str(transaction_date.split(" - ")[1]),
                m00.DATE_SHORT_LOCAL_WITH_DASH)
            transaction_after = datetime.strptime(
                str(transaction_date.split(" - ")[0]),
                m00.DATE_SHORT_LOCAL_WITH_DASH)
            page = received_json_data['page']

            transactions = am.Transaction.objects.filter(
                transaction_type__icontains=transaction_type,
                created_at__lte=transaction_before,
                created_at__gte=transaction_after
            ).select_related("customer").filter(
                Q(customer__complete_name__icontains=customer_name_or_id) |
                Q(customer__identity_number__icontains=customer_name_or_id))

            transactions_list = m00.pagination(page, 1, transactions)

            html = render_to_string(
                        template_name="transaction/transactions-table.html", 
                        context={
                            "transactions": transactions_list,
                        }
                    )
            data_dict = {"html": html}


        elif action == "get_my_customers":
            initials = received_json_data['initials']
            my_customers = am.Customer.objects.filter(
                Q(complete_name__icontains=initials) |
                Q(identity_number__icontains = initials))[: 15]
            html = render_to_string(
                        template_name="general-widgets/customers-list.html", 
                        context={
                            "my_customers": my_customers,
                        }
                    )
            data_dict = {"html": html}


        elif action == "delete_customer":
            error = 0
            error_text = ""
            try:
                am.Customer.objects.filter(
                    id=int(received_json_data['customer_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_CUSTOMER, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "delete_transaction":
            error = 0
            error_text = ""
            try:
                am.Transaction.objects.filter(
                    id=int(received_json_data['transaction_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_TRANSACTION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "save_transaction":
            error = 0
            error_text = ""
            
            if received_json_data['transaction_id'] == 0:
                transaction = am.Transaction()
            else:
                transaction = am.Transaction.objects.get(
                    id=int(received_json_data['transaction_id']))
            try:
                transaction.transaction_type = received_json_data['transaction_type']
                transaction.currency = received_json_data['transaction_currency']
                transaction.amount = received_json_data['transaction_amount']
                transaction.rate = received_json_data['transaction_rate']
                transaction.customer = am.Customer.objects.get(id=int(received_json_data['customer_id']))
                transaction.save()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, SAVE_TRANSACTION, " + str(e)
                error = 1

            if received_json_data['transaction_note'] != "" and error == 0:
                try:
                    new_transacton_note = am.TransactionNotes()
                    new_transacton_note.note = received_json_data['transaction_note']
                    new_transacton_note.transaction = transaction
                    new_transacton_note.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, SAVE_TRANSACTION_NOTE, " + str(e)
                    error = 1

            data_dict = {"error": error, "error_text": error_text}

        elif action == "save_customer":
            error = 0
            error_text = ""
            
            if received_json_data['cus_id'] == 0:
                customer = am.Customer()
            else:
                customer = am.Customer.objects.get(
                    id=int(received_json_data['cus_id']))
            try:
                customer.complete_name = received_json_data['customer_name']
                customer.identity_type = received_json_data['customer_type']
                customer.identity_number = received_json_data['customer_id']
                customer.identity_expire_date = received_json_data['customer_expire']
                customer.phone = received_json_data['customer_phone']
                customer.email = received_json_data['customer_email']
                customer.date_of_birth = received_json_data['customer_birth']
                customer.nationality = received_json_data['customer_nationality']
                customer.address = received_json_data['customer_address']
                customer.sex = received_json_data['customer_sex']
                customer.save()
                print(received_json_data['customer_key'])
                old_file = path.join(
                    settings.MEDIA_ROOT, received_json_data['customer_key'] + ".jpg")
                new_file = path.join(
                    settings.MEDIA_ROOT, str(customer.id) + ".jpg")
                move(old_file, new_file)
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER, " + str(e)
                error = 1

            if received_json_data['customer_note'] != "" and error == 0:
                try:
                    new_customer_note = am.CustomerNotes()
                    new_customer_note.note = received_json_data['customer_note']
                    new_customer_note.customer = customer
                    new_customer_note.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER_NOTE, " + str(e)
                    error = 1

            data_dict = {"error": error, "error_text": error_text}


        return JsonResponse(data=data_dict, safe=False)