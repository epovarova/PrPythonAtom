from flask import Flask, request, jsonify

app = Flask(__name__)

class PrefixTreeNode:
    def __init__(self, value = None, frequency = None):
        self.children = {}
        self.value = value
        self.frequency = frequency

class PrefixTree:
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #Решать вам. Можно, конечно, обходить все ноды, но это долго. Дешевле чуток проиграть по памяти, зато отдавать быстро (скажем можно взять кучу)
    #В терминальных (конечных) нодах может лежать json с топ актерами.
    def __init__(self):
        self.root = PrefixTreeNode()
    def TrieInsert(self, key, value):
        node = self.root
        for i in len(key):
            child = GetChild(node, key[i])
            if child = None:
                child = TrieCreateNode()
                SetChild(node, key[i], child)
            node = child
        node.value = value
        

def init_prefix_tree(filename):
    #TODO в данном методе загружаем данные из файла. Предположим вормат файла "Строка, чтобы положить в дерево" \t "json значение для ноды" \t частота встречаемости


@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()
