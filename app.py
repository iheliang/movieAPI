from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # 本地 MySQL 服务
        user='heliang',
        password='123123',
        database='movie'
    )
    return connection


@app.route('/movies', methods=['GET'])
def get_movies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 获取用户传递的 limit 参数，默认是 10
    limit = request.args.get('limit', default=10, type=int)

    # 获取用户传递的 min_rating 参数，默认是不对评分进行过滤
    min_rating = request.args.get("min_rating", default=None, type=float)

    # 直接使用数据库的中文列名查询
    query = """
    SELECT
        标题,
        导演,
        主演,
        类型,
        地区,
        语言,
        上映日期,
        播放链接,
        封面图片,
        剧情简介,
        评分
    FROM movies
    """
    if min_rating is not None:
        # query += " WHERE 评分 > %s"
        # cursor.execute(query + "LIMIT %s", (min_rating, limit))

        query += " WHERE 评分 > %s"
        query += " LIMIT %s"
        print("查询语句:", query)
        cursor.execute(query, (min_rating, limit))
    else:
        cursor.execute(query + "LIMIT %s", (limit,))
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(movies), 200


# 一个简单的GET请求示例

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# 一个带参数的GET请求示例


@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})


@app.route('/getmovie')
def getmovie():
    pass
    # 一个POST请求示例


@app.route('/api/add', methods=['POST'])
def add():
    # 假设客户端以JSON格式发送数据
    data = request.json
    if 'a' not in data or 'b' not in data:
        return jsonify({"error": "Invalid input"}), 400
    a = data['a']
    b = data['b']
    result = a + b
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
