from piazza_api import Piazza
import html2text
import time


EMAIL = None
PASSWORD = None
CLASSCODE = None


def get_information(inputEmail, inputPassword, inputClasscode):
    # Store information
    EMAIL = inputEmail
    PASSWORD = inputPassword
    CLASSCODE = inputClasscode

    p = Piazza()
    p.user_login(email=EMAIL, password=PASSWORD)
    course = p.network(CLASSCODE)  # CIS 262 class code
    h = html2text.HTML2Text()
    i = 0
    posts = course.iter_all_posts(limit=50)
    # The first element is the month, and then followed by the respective question!
    list_of_questions_and_month = (
        []
    )  # This stores the information from the piazza class!
    for post in posts:
        try:
            time.sleep(0.25)
            post_question = post["history"][0]["content"]
            post_time = post["history"][0]["created"]
            post_month = int(post_time[5:7])
            post_question_text = h.handle(post_question)
            # Formatting the question
            post_question_text = post_question_text.replace("\n", " ")
            list_of_questions_and_month.append([post_month, post_question_text])
            i = i + 1
        except:
            time.sleep(0.1)
    return list_of_questions_and_month
