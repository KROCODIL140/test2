from flask import Flask, render_template

app = Flask(__name__)


# Главная страница
@app.route("/")
def hello():
    return "<html><head></head><body>Hello World!</body></html>"


# Новая страница с передачей данных в шаблон
@app.route("/data_to")
def data_to():
    # Создаем переменные с данными для передачи в шаблон
    some_pars = {'user': 'Ivan', 'color': 'red'}
    some_str = 'Hello my dear friends!'
    some_value = 10

    # Передаем данные в шаблон и вызываем его
    return render_template('simple.html',
                           some_str=some_str,
                           some_value=some_value,
                           some_pars=some_pars)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
