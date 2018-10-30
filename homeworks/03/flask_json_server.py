from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    if request.method == 'POST':
        value = request.json
        if version=='1':
            data = {"version":1,"predict":value['predict']}
        if version=='0':
            data = {"version":0,"predict":value['old_predict']}
        return jsonify(data)
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа {"version":1, "predict":<predict_value>}
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()
