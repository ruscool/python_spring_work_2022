# todo: Сделать рефакторинг кода задачи 35.
#  1. Реализовать из класса DB синглтон. Экземляр класса должен быть единственным.
#  2. Сделать класс View абстрактным, а также метод render() абстрактным
#  3. Реализовать  фабрику FabConsoleView в которой пораждаются экзепляры
#     классов TestView, QuestionView и AuthView

# 1.
# class DB:
#     __instance__ = None
#
#     def __init__(self, name, user, password):
#         self.name = name
#         self.user = user
#         self.password = password
#         if DB.__instance__ is None:
#             DB.__instance__ = self
#         else:
#             raise Exception("We can not creat another class")
#
#     @staticmethod
#     def get_instance():
#         # We define the static method to fetch instance
#         if not DB.__instance__:
#             DB()
#         return DB.__instance__
#
#     def get_connection(self):
#         with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as self.conn:
#             with self.conn.cursor() as cur:
#                 cur.execute(f"""SELECT *  FROM profile
#                     """)
#                 res = cur.fetchall()
#
#         return self.conn


# 2.
# from abc import ABC, abstractmethod
# class View(ABC):
#     """ 'Абстрактный' класс для потомков """
#     @abstractmethod
#     def render(self):
#         print('Virtual')
#
#
# class RegistrationView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку регистрации пользователя"""
#
#
# class LoginView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""


# 3.

class View():
    """ 'Абстрактный' класс для потомков """

    def render(self):
        pass

#TestView, QuestionView и AuthView
class QuestionView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self):
        """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
        print('class', type.__class__)


class TestView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self):
        """Метод реализует отрисовку регистрации пользователя"""
        print('class', type.__class__)

class AuthView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self):
        """Метод реализует отрисовку регистрации пользователя"""
        print('class', type.__mro__)

class ViewView:
    def getView(self, metod_view):
        if metod_view == 'QuestionView':
            return QuestionView()
        elif metod_view == 'RegistrationView':
            return TestView()
        elif metod_view == 'AuthView':
            return AuthView()
        else:
            pass


obj = ViewView()
method = obj.getView("AuthView")
method.render()
