from piazza_api import Piazza
import html2text
import json
import time


EMAIL = None
PASSWORD = None
CLASSCODE = None


def get_information(inputEmail, inputPassword, inputClasscode):
    EMAIL = inputEmail
    PASSWORD = inputPassword
    CLASSCODE = inputClasscode


""" with open('credentials.json') as f:
    credentials = json.load(f)
    EMAIL = credentials.get("email", None)
    PASSWORD = credentials.get("password", None)
    CLASSCODE = credentials.get("classcode", None) """


def main():
    p = Piazza()
    p.user_login(email=EMAIL, password=PASSWORD)
    course = p.network(CLASSCODE)  # CIS 262 class code
    h = html2text.HTML2Text()
    i = 0
    posts = course.iter_all_posts(limit=50)
    # The first element is the month, and then followed by the respective question!
    list_of_questions_and_month = []
    for post in posts:
        try:
            time.sleep(0.25)
            post_question = post["history"][0]["content"]
            post_time = post["history"][0]["created"]
            post_month = int(post_time[5:7])
            post_question_text = h.handle(post_question)
            print(post_question_text)
            # Formatting the question
            post_question_text = post_question_text.replace("\n", " ")
            print(post_month)
            list_of_questions_and_month.append([post_month, post_question_text])
            print(i)
            i = i + 1
        except:
            time.sleep(0.1)
    print(list_of_questions_and_month)


if __name__ == "__main__":
    main()

# To run : virtualenv .venv, source .venv/bin/activate, python run_code.py
