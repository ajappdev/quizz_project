# GENERAL IMPORTATIONS
import pandas as pd
import numpy as np
# APP IMPORTATIONS
import app.models as am

# Declaring variables
questions_types = [
    "Multiple Choices",
    "True or False",
    "Free Text"]

def check_question(question_type: str,
        choices_list: list,
        right_answer: str,
        country: str,
        question: str,
        sub_category: str):

    error_return = ""

    # Check if the question was provided
    if question == "":
        error_return = "The question cannot be empty!"

    # Check if the answer was provided
    elif right_answer == "":
        error_return = "The answer cannot be empty!"

    # Check if a the type of the question is valid
    elif question_type.lower() not in [q.lower() for q in questions_types]:
        error_return = "The question type is not valid!"

    # Check if a free text question was provided with choices
    elif len(choices_list) > 0 and question_type == "Free Text":
        error_return = "A free text question cannot be provided with a choice!"

    # Check if a true/false question was provided but the choices list contain
    # more than two options
    elif question_type == "True or False" and len(choices_list) > 2:
        error_return = "A true/false question cannot be provided with more than 2 choices!"

    # Check if a true/false question was provided but neither true or false
    # figure in the lise of choices
    elif question_type == "True or False" and (
            'true' not in [c.lower() for c in choices_list] or
            'false' not in [c.lower() for c in choices_list]):
        error_return = "A true/false question was provided but neither true nor false is in the list of choices!"

    # Check if a true/false question was provided but neither true or false
    # figure in the right answer
    elif question_type == "True or False" and\
            right_answer.lower() != 'right' and right_answer.lower() != 'false':
        error_return = "A true/false question was provided but either true or false was not provided!"

    # Check if a multiple choices question was provided but the choices 
    # list contains less than 2 options
    elif question_type == "Multiple Choices" and\
            len(choices_list) < 2:
        error_return = "A multiple choices question was provided but the choices list contains less than 2 options!"

    # Check if a multiple choices question was provided but the right
    # answer does not figure in the list of choices
    elif question_type == "Multiple Choices" and\
            right_answer not in choices_list:
        error_return = "A multiple choices question was provided but the answer does not figure in the list of choices!"

    # Check if the country was provided and exists
    elif len(am.Country.objects.filter(name=country)) == 0:
        error_return = "The country does not exist!"

    # Check if the country was provided and exists
    elif len(
            am.SubCategory.objects.filter(name=sub_category)) == 0:
        error_return = "The sub category does not exist!"

    # Check if a all elements are provided and are valid  
    else:
        elements_dict = {
            "country": country,
            "question": question,
            "right_answer": right_answer,
            "sub_category": sub_category}

        for k, v in elements_dict.items():
            if v == "":
                error_return = "The " + str(k) + " cannot be empty!"

    return error_return

def create_question(
        question_type: str,
        choices_list: list,
        right_answer: str,
        country: str,
        question: str,
        sub_category: str
    ):

    check = check_question(question_type,
        choices_list,
        right_answer,
        country,
        question,
        sub_category)

    if check == "":
        # Create the question

        # IF the question already exists?
        if len(am.Question.objects.filter(question=question)) > 0:
            new_question = am.Question.objects.filter(question=question)[0]
            new_question.country = am.Country.objects.filter(name=country)[0]
            new_question.sub_category = am.SubCategory.objects.filter(
                name=sub_category)[0]
            new_question.type = question_type
            new_question.save()

            new_answer = am.Answer.objects.get(question=new_question)
            new_answer.answer = right_answer
            new_answer.save()
            
            am.Choice.objects.filter(question=new_question).delete()
            for choice in choices_list:
                new_choice = am.Choice()
                new_choice.choice = choice
                new_choice.question = new_question
                new_choice.save()

        # IF Its a new question?
        else:
            new_question = am.Question()
            new_question.country = am.Country.objects.filter(name=country)[0]
            new_question.sub_category = am.SubCategory.objects.filter(
                name=sub_category)[0]
            new_question.question = question
            new_question.type = question_type
            new_question.save()

            new_answer = am.Answer()
            new_answer.answer = right_answer
            new_answer.question = new_question
            new_answer.save()

            for choice in choices_list:
                new_choice = am.Choice()
                new_choice.choice = choice
                new_choice.question = new_question
                new_choice.save()

        return ""
    else:
        return check


def check_bulk_upload(file_path: str):
    
    error_return = ""
    try:
        dfs = pd.read_excel(file_path)
    except Exception as e:
        error_return = "Cannot read excel file: " + str(e)
        return error_return
    # Check if the file contains the right columns
    if dfs.columns.tolist() != [
            'Question',
            'Type',
            'SubCategory',
            'Country',
            'Choice1',
            'Choice2',
            'Choice3',
            'Choice4',
            'Choice5',
            'Choice6',
            'Answer']:
        error_return = "Wrong questions file!"
    return error_return

def bulk_upload(file_path: str):
    dfs = pd.read_excel(file_path)
    dfs = dfs.replace(np.nan, "")

    dfs['error'] = ""
    def treat_question(
                question_type,
                question_choices,
                question_answer,
                question_country,
                question_text,
                question_sub_category):

        error_message = ""

        try: 
            error_message = create_question(
                question_type,
                question_choices,
                question_answer,
                question_country,
                question_text,
                question_sub_category
            )
        except Exception as e:
            error_message = e

        return error_message

    dfs["error"] = dfs.apply(
        lambda x: treat_question(
                x.Type,
                [x.Choice1,
                x.Choice2,
                x.Choice3,
                x.Choice4,
                x.Choice5,
                x.Choice6],
                x.Answer,
                x.Country,
                x.Question,
                x.SubCategory
            ), axis=1)

    return dfs