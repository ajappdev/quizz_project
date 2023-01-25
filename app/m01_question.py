# APP IMPORTATIONS
import app.models as am

# Declaring variables
questions_types = [
    "Multiple Choices",
    "Unique choice",
    "True or False",
    "Free Text"]

def create_question(
        question_type: str,
        choices_list: list,
        right_answer: str,
        country: str,
        category: str,
        question: str,
        region: str,
        sub_category: str
    ):

    # Check if the question was provided
    if question == "":
        pass

    # Check if the answer was provided
    elif right_answer == "":
        pass

    # Check if a the type of the question is valid
    elif question_type.lower() not in [q.lower() for q in questions_types]:
        pass

    # Check if a free text question was provided with choices
    elif len(choices_list) > 0 and question_type == "Free Text":
        pass

    # Check if a true/false question was provided but the choices list contain
    # more than two options
    elif question_type == "True or False" and len(choices_list) > 2:
        pass

    # Check if a true/false question was provided but neither true or false
    # figure in the lise of choices
    elif question_type == "True or False" and (
        'true' not in [c.lower() for c in choices_list] or
        'false' not in [c.lower() for c in choices_list]):
        pass

    # Check if a true/false question was provided but neither true or false
    # figure in the right answer
    elif question_type == "True or False" and\
        right_answer.lower() != 'right' and right_answer.lower() != 'false':
        pass

    # Check if a multiple/unique choice question was provided but the choices 
    # list contains less than 2 options
    elif question_type in ["True or False", "Multiple Choices"] and\
            len(choices_list) < 2:
        pass

    # Check if a multiple/unique choice question was provided but the right
    # answer does not figure in the list of choices
    elif question_type in ["True or False", "Multiple Choices"] and\
            right_answer not in choices_list:
        pass

    # Check if the country was provided and exists
    elif country == "" or len(am.Country.objects.filter(name=country)) == 0:
        pass

    # Check if the country was provided and exists
    elif region == "" or len(am.Region.objects.filter(name=region)) == 0:
        pass

    # Check if the country was provided and exists
    elif category == "" or len(am.Category.objects.filter(name=category)) == 0:
        pass

    # Check if the country was provided and exists
    elif sub_category == "" or len(
            am.SubCategory.objects.filter(name=sub_category)) == 0:
        pass

    # Check if a all elements are provided and are valid  
    else:
        elements_dict = {
            "country": country,
            "category": category,
            "question": question,
            "region": region,
            "right_answer": right_answer,
            "sub_category": sub_category}

        for k, v in elements_dict.items():
            if v == "":
                pass
                return

    # Create the question 
    new_question = am.Question()
    new_question.category = am.Category.objects.filter(name=category)[0]
    new_question.country = am.Country.objects.filter(name=country)[0]
    new_question.region = am.Region.objects.filter(name=region)[0]
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