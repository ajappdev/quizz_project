# DJANGO DECLARATIONS
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.templatetags.static import static
from django.template.loader import render_to_string
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# GENERAL DECLARATIONS
import pandas as pd
import os
from django.http import JsonResponse, HttpResponse
import json
from datetime import date, datetime
from os import path
from shutil import move
from io import BytesIO

# APP DECLARATIONS
import app.models as am
import app.forms as af
import app.m00_common as m00
import app.m01_question as m01

# DECLARING FONCTIONS


def register(request):
    register_form = af.RegisterForm()
    error_to_show = ""
    if request.method == "POST":
        register_form = af.RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()

            user_profile = am.UserProfile()
            user_profile.user = user
            user_profile.role = "Student"
            user_profile.username = request.POST['username']
            user_profile.save()

            login(request, user)

            return redirect("/")

        else:
            registration_errors = json.loads(register_form.errors.as_json())
            for k, v in registration_errors.items():
                error_to_show = v[0]['message']

    template = 'registration/register.html'
    context = {
        "register_form": register_form,
        "error_to_show": error_to_show}
    return render(request, template, context)


def landing_page(request):
    if request.user.id:
        if request.user.user_profile.role == "Administrator":
            return redirect("administrator/dashboard/")
        if request.user.user_profile.role == "Student":
            return redirect("student/dashboard/")

    template = "landing.html"
    context = {}

    return render(request, template, context)


@login_required(login_url='login/')
def dashboard_admin(request):
    template = 'administrator/dashboard.html'
    context = {}
    return render(request, template, context)


@login_required(login_url='login/')
def dashboard_student(request):
    template = 'student/dashboard.html'
    context = {}
    return render(request, template, context)


def quizz(request):
    template = 'quizz/quizz.html'
    regions = am.Region.objects.all()
    categories = am.Category.objects.all()
    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()

    context = {
        "regions": regions,
        "categories": categories,
        "countries": countries,
        "sub_categories": sub_categories}
    return render(request, template, context)


@login_required(login_url='login/')
def admin_settings(request):
    template = 'administrator/settings.html'

    regions = am.Region.objects.filter(id__gte=0).order_by("name")
    categories = am.Category.objects.filter(id__gte=0).order_by("name")
    countries = am.Country.objects.filter(id__gte=0).order_by("name")
    sub_categories = am.SubCategory.objects.filter(id__gte=0).order_by("name")
    context = {
        "regions": regions,
        "categories": categories,
        "countries": countries,
        "sub_categories": sub_categories,
        }
    return render(request, template, context)


@login_required(login_url='login/')
def add_question(request):
    countries = am.Country.objects.all()
    sub_categories = am.SubCategory.objects.all()
    template = 'administrator/add-update-question.html'
    context = {
        "countries": countries,
        "sub_categories": sub_categories,
        }
    return render(request, template, context)


@login_required(login_url='login/')
def update_question(request, pk: int):
    template = 'administrator/update-question.html'
    question = am.Question.objects.get(id=pk)
    context = {"question": question}
    return render(request, template, context)


@login_required(login_url='login/')
def bulk_upload_questions(request):

    template = 'administrator/bulk-upload-questions.html'
    context = {
        }
    return render(request, template, context)

@login_required(login_url='login/')
def initial_settings_upload(request):
    m00.initial_settings()
    template = 'administrator/initial-settings.html'
    context = {
        }
    
    return render(request, template, context)


@login_required(login_url='login/')
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

            success_questions = treatment_result.loc[
                (treatment_result['error'] == ''), 'Question'].count()
            failed_questions = treatment_result.loc[
                (treatment_result['error'] != ''), 'Question'].count()
            
            treatment_result = treatment_result.loc[
                (treatment_result['error'] != '')]

            html = render_to_string(
                template_name="administrator/widgets/bulk-treatment.html",
                context={
                    "treatment_result": treatment_result,
                    "success_questions": success_questions,
                    "failed_questions": failed_questions,      
                }
            )
            data_dict = {"error": "", "html": html}
        else:
            data_dict = {"error": error_upload} 

        return JsonResponse(data=data_dict, safe=False)

@login_required(login_url='login/')
def download_excel_template(request):
    df = pd.DataFrame(columns=[
            'N',
            'Question',
            'Choice 1',
            'Choice 2',
            'Choice 3',
            'Choice 4',
            'Answer',
            'Country',
            'Sub Type'])
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index = False)
        writer.save()
        # Set up the Http response.
        filename = 'questions_template.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response

def ajax_calls(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        function = received_json_data['function']

        if function == "get_current_regions":
            current_regions = list(
                am.Region.objects.all().values("id", "name"))
            data_dict = {"current_regions": current_regions}

        elif function == "look_for_childs":
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


        elif function == "save_question_form":

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
                    received_json_data['question_text'],
                    received_json_data['question_choices'],
                    received_json_data['question_answer'],
                    received_json_data['question_country'],
                    received_json_data['question_sub_category'],
                )
            except Exception as e:
                error_message = e

            data_dict = {"error_message": str(error_message)}

        elif function == "get_current_categories":
            current_categories = list(
                am.Category.objects.all().values("id", "name"))
            data_dict = {"current_categories": current_categories}

        elif function == "add_country":
            error = 0
            error_text = ""
            new_country_id = 0

            if received_json_data['country_name'] != "":
                try:
                    new_country = am.Country()
                    new_country.name=received_json_data['country_name']
                    new_country.save()

                    for region in received_json_data['region_id']:
                        new_country.region.add(am.Region.objects.get(id=int(region)))
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

        elif function == "delete_country":
            error = 0
            error_text = ""
            try:
                am.Country.objects.filter(
                    id=int(received_json_data['country_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_COUNTRY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "update_country":
            error = 0
            error_text = ""
            if received_json_data['country_name'] != "":
                try:
                    am.Country.objects.filter(
                        id=int(received_json_data['country_id'])).update(
                            name=received_json_data['country_name'])
                    country = am.Country.objects.get(
                        id=int(received_json_data['country_id']))
                    country.region.clear()
                    for region in received_json_data['country_region']:
                        country.region.add(am.Region.objects.get(id=int(region)))
                        country.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_COUNTRY, 1, " + str(e)
                    error = 1
            else:
                error_text = "Country name cannot be empty!"
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "add_sub_category":
            error = 0
            error_text = ""
            new_sub_category_id = 0
            if received_json_data['sub_category_name'] != "":
                try:
                    new_sub_category = am.SubCategory()
                    new_sub_category.name=received_json_data['sub_category_name']
                    new_sub_category.save()
                    for category in received_json_data['parent_category_id']:
                        new_sub_category.category.add(am.Category.objects.get(id=int(category)))
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

        elif function == "delete_sub_category":
            error = 0
            error_text = ""
            try:
                am.SubCategory.objects.filter(
                    id=int(received_json_data['sub_category_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_SUB_CATEGORY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "update_sub_category":
            error = 0
            error_text = ""
            if received_json_data['sub_category_name'] != "":
                try:
                    am.SubCategory.objects.filter(
                        id=int(received_json_data['sub_category_id'])).update(
                            name=received_json_data['sub_category_name'])
                    sub_category = am.SubCategory.objects.get(
                        id=int(received_json_data['sub_category_id']))
                    sub_category.category.clear()
                    for category in received_json_data['sub_category_parent_category']:
                        sub_category.category.add(am.Category.objects.get(id=int(category)))
                        sub_category.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, UPDATE_SUB_CATEGORY, 1, " + str(e)
                    error = 1
                data_dict = {"error": error, "error_text": error_text}
            else:
                error_text = "Sub category name cannot be empty!"
                error = 1
        elif function == "add_region":
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

        elif function == "delete_question":
            error = 0
            error_text = ""
            try:
                am.Question.objects.filter(
                    id=int(received_json_data['question_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_QUESTION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "delete_region":
            error = 0
            error_text = ""
            try:
                am.Region.objects.filter(
                    id=int(received_json_data['region_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_REGION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "update_region":
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

        elif function == "add_category":
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

        elif function == "delete_category":
            error = 0
            error_text = ""
            try:
                am.Category.objects.filter(
                    id=int(received_json_data['category_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_CATEGORY, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif function == "update_category":
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

        elif function == "filter_questions_list_for_quizz":
            
            type_quizz = int(received_json_data['type_quizz'])
            if type_quizz == 1:
                nb_q = 10
            elif type_quizz == 2:
                nb_q = 5

            error_text = ""
            questions = am.Question.objects.all()
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

            questions = questions.values_list('id', flat=True)

            try:
                import random
                questions = random.sample(list(questions), min(len(questions), nb_q))
                questions = am.Question.objects.filter(id__in=questions)
            except Exception as e:
                error_text = e

            if len(questions) < nb_q:
                error_text = "Not enough questions for the chosen criteria!"

            html = render_to_string(
                        template_name="quizz/questions-quizz.html", 
                        context={
                            "questions": questions,
                        }
                    )
            data_dict = {"html": html, "error_text": str(error_text)}

        elif function == "filter_questions_list":
    
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

            length_result = len(questions)
            questions_list = m00.pagination(page, 10, questions)

            html = render_to_string(
                        template_name="administrator/questions-table.html", 
                        context={
                            "questions": questions_list,
                            "length_result": length_result,
                        }
                    )
            data_dict = {"html": html}


        return JsonResponse(data=data_dict, safe=False)