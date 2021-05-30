# подключение библиотек
import sqlite3 as ql  # для взаимодействия с БД SQLite
import sys  # для работы с интепритатором Python
from PyQt5 import QtWidgets as qw  # для GUI
from PyQt5 import uic  # для конвертации разметки GUI
import MainForm as mf
import fmCh


class TABook(qw.QMainWindow, mf.Ui_MainWindow):  # создание класса TABook от класса QMainWindow
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
#        uic.loadUi('MainForm.ui', self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.setupUi(self)
        self.ad = TfmCh()  # Создаем форму для изменений
        self.ad.setWindowTitle('Изменение записи')  # задаю заголовок формы-изменения
        self.f_add = TfmAdd()  # Создаем форму для добавления записи
        self.f_add.setWindowTitle('Добавление записи')  # задаю заголовок формы-добавления
        self.f_add.tv = self.twBook  # Сохранение записи в основном окне

        self.acAdd.triggered.connect(self.ev_add)  # связывание сигнала действия-добавления с моим слотом
        self.acUpd.triggered.connect(self.ev_upd)  # связывание сигнала действия-изменения с моим слотом
        self.acDel.triggered.connect(self.ev_del)  # связывание сигнала действия-удаления с моим слотом

        self.twBook.itemSelectionChanged.connect(self.ev_sel)    # связывание сигнала выбора записи с моим слотом

        con = ql.connect("AddressBook.db")  # подключение к БД

        try:
            cur = con.cursor()  # открыла курсор к БД
            # Проверяю наличие таблицы address_book в БД:
            cur.execute("select count(*) from sqlite_master where type='table' and name='address_book'")
            recs = cur.fetchall()  # сохранение результата выборки в список
            is_bd = False
            if len(recs):
                if recs[0][0]:
                   is_bd = True

            if not is_bd:
                cur.execute('create table "address_book" ('
                            '"id"	integer not null unique,'
                            '"name"	text,'
                            '"fio"	text,'
                            '"phone"	text,'
                            '"mail"	text,'
                            '"note"	text,'
                            'primary key("id" autoincrement))')  # создаем таблицу в БД
                item = ('Александр', 'Петушков', '+7(902)6-23-65-34', 'PetyhA@mail.ru', 'друг')
                cur.execute('insert into address_book (name,fio,phone,mail,note) values (?, ?, ?, ?, ?)', item)
                item = ('Мария', 'Зайцева', '+7(902)6-45-23-54', 'MariaZaiceva@mail.ru', 'соседка')
                cur.execute('insert into address_book (name,fio,phone,mail,note) values (?, ?, ?, ?, ?)', item)
                item = ('Илья', 'Сорокин', '+7(902)6-34-52-67', 'Soroka@mail.ru', 'родственник')
                cur.execute('insert into address_book (name,fio,phone,mail,note) values (?, ?, ?, ?, ?)', item)
                con.commit()

            cur.execute("select * from address_book")  # выполнение запроса к БД на выборку данных
            recs = cur.fetchall()  # сохранение результата выборки в список

            self.twBook.clear()  # очистка виджета-списка

            colsWidth = (0, 70, 160, 120, 200)  # картеж ширины столбцов
            for i in range(5):  # цикл выборки (по элементам списка)
                self.twBook.setColumnWidth(i, colsWidth[i])  # задание ширины столбцов

            for rec in recs:  # цикл по результатам выборки (по элементам списка)
                qw.QTreeWidgetItem(self.twBook, map(str, rec))  # создание строк в виджет-списке

            cur.close()  # закрытие курсора к БД

        except ql.Error as er:  # если возникла ошибка
            self.sbMainForm.showMessage('Ошибка при подключении к БД: {0}'.format(er))  # вывести ошибку в статусе-формы
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД

    def ev_add(self):  # слот для сигнала действия-добавления
        self.f_add.leId.setText('')  # очищаем строку с идентификатором
        self.f_add.leName.setText('')  # очищаем строку с именем
        self.f_add.leFamily.setText('')  # очищаем строку с фамилией
        self.f_add.lePhone.setText('')  # очищаем строку с телефоном
        self.f_add.leMail.setText('')  # очищаем строку с майлом
        self.f_add.leNote.setText('')  # очищаем строку с заметками
        self.f_add.show()  # показываем окно

    def ev_sel(self):  # слот для сигнала разблокировки кнопок редактирования и удаления записей, при выборе записи
        sel_items = self.twBook.selectedItems()  # список выделеных записей
        if len(sel_items):  # проверяю, что список не пуст
            self.acUpd.setEnabled(True)  # делаю доступной кнопку обновления
            self.acDel.setEnabled(True)  # делаю доступной кнопку удаления
        else:   # если список пуст,то
            self.acUpd.setEnabled(False)  # делаю недоступной кнопку обновления
            self.acDel.setEnabled(False)  # делаю недоступной кнопку удаления

    def ev_upd(self):   # слот для сигнала действия-редактирования
        sel_items = self.twBook.selectedItems()  # получаю список выделенных записей
        if len(sel_items):  # проверяю, что список не пуст
            self.ad.sel_item = sel_items[0]  # у поля подчиненной формы задаю ссылку на 1 выделенную запись
            self.ad.leId.setText(self.ad.sel_item.text(0))  # заносим в поле ввода текст 0 элемента записи
            self.ad.leName.setText(self.ad.sel_item.text(1))  # заносим в поле ввода текст 1 элемента записи
            self.ad.leFamily.setText(self.ad.sel_item.text(2))  # заносим в поле ввода текст 2 элемента записи
            self.ad.lePhone.setText(self.ad.sel_item.text(3))  # заносим в поле ввода текст 3 элемента записи
            self.ad.leMail.setText(self.ad.sel_item.text(4))  # заносим в поле ввода текст 4 элемента записи
            self.ad.leNote.setText(self.ad.sel_item.text(5))  # заносим в поле ввода текст 5 элемента записи
            self.ad.show()  # показываю форму

    def ev_del(self):  # слот для сигнала действия-удаления
        sel_items = self.twBook.selectedItems()   # получаю список выделенных записей
        con = ql.connect("AddressBook.db")  # подключение к БД
        try:
            cur = con.cursor()  # открыла курсор к БД
            for sel_item in sel_items:  # бежим по списку выделенных записей
                # выполняю запрос на удаление данных в БД, соответствующих данным выделенной строки:
                cur.execute(f"delete from address_book where id={sel_item.text(0)}")
                # удаляю запись главной формы:
                self.twBook.takeTopLevelItem(self.twBook.indexOfTopLevelItem(sel_item))
            con.commit()  # сделать коммит для данной БД
            cur.close()  # закрытие курсора к БД

        except ql.Error as er:  # если возникла ошибка
            self.sbMainForm.showMessage('Ошибка при подключении к БД: {0}'.format(er))  # вывести ошибку в статусе-формы
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД


class TfmCh(qw.QDialog, fmCh.Ui_fmCh):  # создание класса TfmCh от класса QDialog
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
#        uic.loadUi("fmCh.ui", self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.setupUi(self)
        self.pbOk.clicked.connect(self.ev_save)  # связывание сигнала действия-нажатия кнопки ок с моим слотом
        self.sel_item = qw.QTreeWidgetItem()  # создание поля,которое будет ссылаться на выделенную строку главной формы

    def ev_save(self):  # слот для сигнала действия-сохрания
        con = ql.connect("AddressBook.db")  # подключение к БД
        try:
            cur = con.cursor()  # открыла курсор к БД
            cur.execute(f'update address_book set '
                        f'name="{self.leName.text()}", '
                        f'fio="{self.leFamily.text()}", '
                        f'phone="{self.lePhone.text()}", '
                        f'mail="{self.leMail.text()}", '
                        f'note="{self.leNote.text()}" '
                        f'where id={self.leId.text()}')   # выполнить обновления данных в БД
            con.commit()  # сделать коммит для данной БД
            cur.close()  # закрытие курсора к БД

        except ql.Error as er:  # если возникла ошибка
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД

        self.sel_item.setText(1, self.leName.text())  # заполнение поля "Имя" текстом
        self.sel_item.setText(2, self.leFamily.text())  # заполнение поля "Фамилия" текстом
        self.sel_item.setText(3, self.lePhone.text())  # заполнение поля "Телефон" текстом
        self.sel_item.setText(4, self.leMail.text())  # заполнение поля "Почта" текстом
        self.sel_item.setText(5, self.leNote.text())  # заполнение поля "Заметки" текстом

        self.close()  # закрытие формы


class TfmAdd(qw.QDialog, fmCh.Ui_fmCh):  # создание класса TfmCh от класса QDialog
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
#        uic.loadUi("fmCh.ui", self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.setupUi(self)
        self.pbOk.clicked.connect(self.ev_save)  # связывание сигнала действия-нажатия кнопки ок с моим слотом
        self.tv = qw.QTreeWidget()   # создание поля,которое будет ссылаться на элемент со списком строк главной формы

    def ev_save(self):
        con = ql.connect("AddressBook.db")  # подключение к БД
        try:
            cur = con.cursor()  # открытие курсора к БД
            item = (self.leName.text(),
                    self.leFamily.text(),
                    self.lePhone.text(),
                    self.leMail.text(),
                    self.leNote.text())  # создание картежа из введенных данных

            # вставка данных из картежа в БД:
            cur.execute('insert into address_book (name,fio,phone,mail,note) values (?, ?, ?, ?, ?)', item)
            # получение id,сохранной в БД строки:
            cur.execute('select seq from sqlite_sequence where name="address_book"')
            recs = cur.fetchall()  # сохранение результата выборки в список
            con.commit()  # сделать коммит для данной БД
            cur.close()  # закрытие курсора к БД
            if len(recs):  # проверяю,что список строк, полученный из БД не пустой
                item = (recs[0][0],) + item  # дополнила картеж идентификатором
                for tv_item in self.tv.selectedItems():  # бегу по всем выделенным строкам главной формы
                    tv_item.setSelected(False)  # снимаем выделение
                # добавляю выделенную строку в главную форму:
                qw.QTreeWidgetItem(self.tv, map(str, item)).setSelected(True)

        except ql.Error as er:  # если возникла ошибка
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД

        self.close()  # закрытие окна


def main():
    app = qw.QApplication(sys.argv)  # Создаю объект, который управляет GUI, на основе класса QApplication
    ab = TABook()  # Создаю объект класса TABook
    ab.show()  # Показываю окно
    app.exec_()  # Запускаю обработку событий в нашем окне


if __name__ == '__main__':  # Если запускается файл напрямую, а не импортируется
    main()  # то запускается функция main()
