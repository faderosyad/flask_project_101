from flask import Blueprint, render_template, request
from utils.time_helper import getTimestamp
from utils.simple_calculation import simpleAdd, simpleSubtract, simpleMultiply

# Create a Blueprint instance
# The first argument 'main' is the Blueprint's name, used in url_for
# The second argument __name__ helps Flask locate resources like templates
main_bp = Blueprint('main', __name__, template_folder='../templates')

@main_bp.route('/', methods=['GET', 'POST'])
def frontpage():
    dateTime = getTimestamp()
    helloMessage = "Hello World! \n Today date is "
    
    addition_result = None
    subtraction_result = None
    multiplication_result = None

    # Helper function to parse inputs and perform calculation
    def calculate(num1_str, num2_str, operation_func):
        if num1_str and num2_str:
            num1 = float(num1_str)
            num2 = float(num2_str)
            return operation_func(num1, num2)
        elif num1_str is None or num2_str is None: # Should not happen if fields are required, but good for robustness
            return "Please provide both numbers."
        else: # Handles empty strings if they somehow bypass client-side validation
            return "Input fields cannot be empty."

    if request.method == 'POST':
        action = request.form.get('action') # Identifies which form was submitted

        try:
            if action == 'add':
                addition_result = calculate(
                    request.form.get('add_num1'),
                    request.form.get('add_num2'),
                    simpleAdd
                )
            elif action == 'subtract':
                subtraction_result = calculate(
                    request.form.get('sub_num1'),
                    request.form.get('sub_num2'),
                    simpleSubtract
                )
            elif action == 'multiply':
                multiplication_result = calculate(
                    request.form.get('mul_num1'),
                    request.form.get('mul_num2'),
                    simpleMultiply
                )
        except ValueError:
            error_message = "Invalid input. Please enter numbers only."
            if action == 'add': addition_result = error_message
            elif action == 'subtract': subtraction_result = error_message
            elif action == 'multiply': multiplication_result = error_message
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            if action == 'add': addition_result = error_message
            elif action == 'subtract': subtraction_result = error_message
            elif action == 'multiply': multiplication_result = error_message
            
    return render_template('frontpage.html', helloMessage=helloMessage, dateTime=dateTime, 
                           addition_result=addition_result, subtraction_result=subtraction_result, multiplication_result=multiplication_result)

@main_bp.route('/about_me')
def about_me():
    name = "Fade Khalifah Rosyad"
    jobs = "Software Development Engineer"
    linkedin = "https://www.linkedin.com/in/faderosyad/"
    github = "https://github.com/faderosyad"
    return render_template('aboutme.html', name = name, jobs = jobs, linkedin = linkedin, github = github)