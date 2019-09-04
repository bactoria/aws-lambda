
**psycopg2**

https://github.com/jkehler/awslambda-psycopg2 에서 psycopg2-3.7 다운받고 psycopg2 로 이름 바꾸기

&nbsp;

cursor 클래스 사용법은 [여기](http://initd.org/psycopg/docs/cursor.html )에 잘 나와 있음

&nbsp;

### 환경 변수

|key|value|
|-|-|
|DB_NAME|postgres|
|DB_USER|bactoria|

```python
import os

print(os.environ['DB_NAME'])
print(os.environ['DB_USER'])
```