from sqlalchemy import create_engine

from api.models.task import Base

DB_URL = "mysql+pymysql://test:test_pass@db:3306/demo?charset=utf8"
# mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()

# api 모듈의 migrate_db 스크립트를 실행
# docker compose exec demo-app poetry run python -m api.migrate_db;
# docker exec -it {컨테이너 ID}  mysql -uroot -p
# 디비 아이디, 비밀번호 추가하고 권한 추가후 마이그레이션 실행하면 됨