"""
        RDS에 접근하여 데이터를 조작하는 코드
        https://show-me-the-money.tistory.com/68
"""
import os
import psycopg2
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']
# db_port = 5432
conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))


def lambda_handler(event, context):
    try:
        # PostgreSQL Default Port Number
        sql = 'UPDATE test SET name=%s, nickname=%s WHERE id=%s'
        name = 'newName'
        nickname = 'newNickname'
        id = 1

        # RDS 연결
        cursor = conn.cursor()

        # 쿼리 출력
        logger.info(cursor.mogrify(sql, (name, nickname, id,)))

        # 쿼리 실행
        cursor.execute(sql, (name, nickname, id,))

        # 커밋
        conn.commit()

    except Exception as e:
        logger.error(e)
