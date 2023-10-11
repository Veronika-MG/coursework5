import os
from dotenv import load_dotenv

from db_manage.db_manager import PostgresDBManager
from api_engine.hh_engine_class import HeadHunterApiHandler
from utils import insert_employer_data_to_db, insert_vacancy_data_to_db
from db_manage.db_manager import create_db

if __name__ == '__main__':

    load_dotenv()

    create_db(dbname='coursework',
        user='postgres',
        password=os.environ.get('DB_PASSWORD'),
        host='localhost',
        port='5432')

    db = PostgresDBManager(
        dbname='coursework',
        user='postgres',
        password=os.environ.get('DB_PASSWORD'),
        host='localhost',
        port='5432'
    )

    db.drop_tables()
    db.create_tables()

    api_handler = HeadHunterApiHandler()
    vacancy_list = api_handler.get_vacancies_data()
    employers_list = api_handler.get_employer_data()

    insert_employer_data_to_db(employers_list, db)
    insert_vacancy_data_to_db(vacancy_list, db)

    print(db.get_companies_and_vacancies_count())
    print(db.get_all_vacancies())
    print(db.get_avg_salary())
    print(db.get_vacancies_with_higher_salary())
    print(db.get_vacancies_with_keyword('стажер'))

    if not db.conn.closed:
        db.conn.close()
