from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # 本地 MySQL 服务
        user='root',
        password='123123',
        database='movie'
    )
    return connection


# 随机生成21条电影数据的接口
@app.route('/movies/random', methods=['GET'])
def get_random_movies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 随机获取21条电影
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
    ORDER BY RAND()
    LIMIT 21
    """
    cursor.execute(query)
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(movies), 200

# 根据“地区、类型、年份、排序”进行条件查询并分页


@app.route('/movies/filter', methods=['GET'])
def filter_movies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 获取用户传递的过滤参数
    region = request.args.get('region', default=None)
    genre = request.args.get('genre', default=None)
    year = request.args.get('year', default=None, type=int)
    sort_by = request.args.get('sort_by', default='评分')  # 默认按评分排序
    order = request.args.get('order', default='desc')  # 默认降序排序
    page = request.args.get('page', default=1, type=int)  # 页码，默认是第一页
    per_page = 21  # 每页返回21条

    # 动态构建查询语句
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
    WHERE 1=1
    """
    # 过滤条件
    params = []
    if region:
        query += " AND 地区 = %s"
        params.append(region)
    if genre:
        query += " AND 类型 = %s"
        params.append(genre)
    if year:
        query += " AND YEAR(上映日期) = %s"
        params.append(year)

    # 排序和分页
    query += f" ORDER BY {sort_by} {order} LIMIT %s OFFSET %s"
    offset = (page - 1) * per_page
    params.extend([per_page, offset])

    cursor.execute(query, tuple(params))
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(movies), 200

# 随机生成六条电影数据的接口


@app.route('/movies/random6', methods=['GET'])
def get_random_6_movies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 随机获取6条电影
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
    ORDER BY RAND()
    LIMIT 6
    """
    cursor.execute(query)
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(movies), 200

# 随机生成九条电影数据的接口


@app.route('/movies/random9', methods=['GET'])
def get_random_9_movies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 随机获取9条电影
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
    ORDER BY RAND()
    LIMIT 9
    """
    cursor.execute(query)
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(movies), 200


if __name__ == '__main__':
    app.run(debug=True)
