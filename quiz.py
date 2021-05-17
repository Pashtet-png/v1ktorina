# Здесь будет код веб-приложения
from flask import Flask, redirect, url_for, request
from random import randint, shuffle
from db_scripts import get_question, get_quises
import os

list_id = list(range(1, 4))

def show_quises_form():
    quizes = get_quises()

    return render_template('start.html', quizes=quizes)


    
def index():
    global list_id
    shuffle(list_id)

    if request.method == 'GET':
        return show_quises_form()
    else:
        #Получить викторины
        vict_id = reqest.form.get("vict")
        #Показать форму
        quiz_id = get_question(last_id, vict_id)
        redirect(url_for("test"))



def test():
    global list_id
    if len(list_id) > 0:
        q = get_question(list_id[0])
        list_id.remove(list_id[0])
        return '<h1>'+ str(q[1]) + '</h1>' + '<p>' + str(q[2]) + '</p>'  + '<p>' + str(q[3]) + '</p>'  + '<p>' + str(q[4]) + '</p>' + '<p>' + str(q[5]) + '</p>' 


    else:
        return redirect(url_for('result'))



def result():
    return '<h> Иди отсюда, не грузи сервера </h>'

folder = os.getcwd()
app = Flask(__name__, template_folder = folder, static_folder = folder)


app.add_url_rule('/', 'index', index)#Правило для главной стр
app.add_url_rule('/test', 'test', test)#Правильно для страницы с викториной
app.add_url_rule('/result', 'result', result)#Правило для стр с результатом


if __name__ == "__main__":
    app.run()















