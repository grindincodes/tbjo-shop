# 실행
git clone https://github.com/grindincodes/tbjo-shop

## 공통 기본 환경 구성
최신 우분투 운영체제에는 파이썬3이 깔려 있음.  
apt 업데이트  
sudo apt update  
파이썬3 버전 확인. 3.10.XX 여야 함.  
python3 --version  


## 설치방법 1. 가상황경 생성 및 라이브러리 설치 
1. 가상환경 패키지 설치(있으면 설치 X)  
sudo apt install python3.10-venv
2. 가상환경 생성 (현재 폴더에 생성)  
python3 -m venv myvenv
3. 가상환경 활성화(<-> deactivate)  
source myvenv/bin/activate
4. 필요 라이브러리 설치  
pip install -r requirements.txt  
만약 PATH 등록이 없다는 오류가 출력되면 PATH 설정 필요
5. 환경변수 설정  
.env 파일을 프로젝트 루트에 만들고, 필요한 환경변수 설정. = 후에 띄어쓰기 X, 엔터로 각 환경변수 구분!  (장고 시크릿 키 생성 url: https://djecrety.ir/)  
DJANGO_SECRET=‘Insert your django secret in quotes’

## 설치방법 2. 가상환경 없이 설치(ubuntu 22.04 LTS 기반, lsb_release -a 로 확인 가능.)
pip install -r requirements.txt  
필요 라이브러리 설치 후 경로가 PATH에 없다는 오류가 만약 나온다면,  
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/home/ubuntu/.local/bin  
를 추가해준다.  
앞서 언급한 환경변수 설정하기.  

** 가상환경 기반일 시 아래 내용들은 반드시 가상환경 활성화 후 실행 **  

## DB 마이그레이션
DB 스키마, 테이블 내용을 migrate 하는 것.
설정된 DB에 애플리케이션에 필요한 테이블을 생성해주는 명령어라 생각하면 됨.  
그러므로 같은 DB에 대해 새 테이블이 생기지 않는 한, 한 번만 실행해주면 되는 것!  
python manage.py makemigrations  
python manage.py migrate

## 실행
** 개발 서버로 실행 **
python manage.py runserver  
** 아래 예시와 같이 listen할 포트와 ip 주소를 특정할 수 있다. **  
python manage.py runserver 0.0.0.0:8080  
** 백그라운드 실행 **  
python manage.py runserver 0.0.0.0:8080 &  
** 백그라운드 실행 및 서버의 표준 오류, 표준 출력을 파일로 출력하는 명령어 **  
python3 manage.py runserver 0.0.0.0:8080 > server.log 2>&1 &  
** gunicorn wsgi 서버 사용하여 실행방법 **  
gunicorn tbjo-shop.wsgi:application  
gunicorn -b 0.0.0.0:8080 tbjo-shop.wsgi:application  
## 관리자 계정 생성 및 관리자 페이지  
1. 계정 생성
python manage.py createsuperuser  
후
username
email
password
password
입력 후
생성 완료!

2. 관리자 페이지
/admin 경로로 접속하면 됨 (e.g. 127.0.0.1:8000/admin)
username
password
입력 시 로그인이 됨.
상품을 등록하고 삭제하고, 
주문 내역을 관리할 수 있음.

## DB 관련 참고사항
외부 DB 서버를 사용하지 않고, sqlite3 DB 파일을 사용하여 테스트할 수 있다.
이후 DB 설정 필요 시, tbjo_shop/tbjo_shop/settings.py의 아래 내용을 그에 맞게 수정해준다.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default' : {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "mydatabase",
    #     "USER": "mydatabaseuser",
    #     "PASSWORD": "mypassword",
    #     "HOST": "127.0.0.1",
    #     "PORT": "3306",
    # }
}
```
## 이미지 관련 참고사항
사용자/관리자가 업로드한 이미지는 프로젝트 루트 디렉토리의 media 디렉토리에 저장됨. (media/img)

# 배포

### 정적 파일 모으는 명령어  
python manage.py collectstatic  
하면 프로젝트의 루트 디렉토리에 static 폴더가 생긴다.  
이를 웹 서버에서 서비스할 수 있도록 설정하면 됨.  
(개발 후 정적 파일(css,js,img) 수정 되었을 때 이 명령어를 실행 후 웹 서버에 정적파일을 새로 업데이트 해줘야 함.)

### 장고 개발용 서버 vs wsgi 서버
manage.py로 실행할 수 있지만,
gunicorn 패키지를 깔고 wsgi 서버를 장고 애플리케이션과 연결하면 더 적합한 배포 구성이 됨.
