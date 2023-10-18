from abc import ABC, abstractmethod


class AbstractDBManager(ABC):
    """
    Абстрактный класс для менеджера для работы с базами данных
    """

    @abstractmethod
    def get_companies_and_vacancies_count(self):
        """
        Метод получает список всех компаний и количество вакансий у каждой компании
        :return:
        """
        pass

    @abstractmethod
    def get_all_vacancies(self):
        """
        Метод получает список всех вакансий с названией компании, названией вакансии и зарплаты и ссылки на вакансию
        :return:
        """
        pass

    @abstractmethod
    def get_avg_salary(self):
        """
        Метод получает среднюю зарплату по вакансиям
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self):
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, keyword):
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова
        :param keyword:
        :return:
        """
        pass
