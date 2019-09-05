import os
import psycopg2
import logging
from crawler import crawling
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']
# db_port = 5432

# RDS 연결
conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
cursor = conn.cursor()


def lambda_handler(event, context):
    try:
        # SelectAll
        cursor.execute('SELECT * FROM channel');
        channelIdList = cursor.fetchall()

        for channelId in channelIdList:
            channelLog = crawling(channelId[0])

            dt = datetime.datetime.now();
            date = dt.strftime('%Y-%m-%d')
            hour = dt.strftime('%H')

            id = channelId[0]
            subscriber = channelLog['subscriber']

            # PostgreSQL Default Port Number
            sql = '''
            INSERT INTO channel_log("date", "hour", "id", "subscriber")
            VALUES(%s,%s,%s,%s);
            '''

            # 쿼리 출력
            logger.info(cursor.mogrify(sql, (date, hour, id, subscriber)))

            # 쿼리 실행
            cursor.execute(sql, (date, hour, id, subscriber))

            # 커밋
            conn.commit()

    except Exception as e:
        logger.error(e)
