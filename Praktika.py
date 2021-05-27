# подключение библиотек
import sqlite3 as ql  # для взаимодействия с БД SQLite
import sys  # для работы с интепритатором Python
from PyQt5 import QtWidgets as qw  # для GUI
from PyQt5 import uic  # для конвертации разметки GUI


class TABook(qw.QMainWindow):  # создание класса TABook от класса QMainWindow
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
        uic.loadUi('MainForm.ui', self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.ad = TfmCh()  # Создаем форму для изменений
        self.f_add = TfmAdd()
        self.f_add.tv = self.twBook

        self.acAdd.triggered.connect(self.ev_add)  # связывание сигнала действия-добавления с моим слотом
        self.twBook.itemSelectionChanged.connect(self.ev_sel)
        self.acUpd.triggered.connect(self.ev_upd)
        self.acDel.triggered.connect(self.ev_del)

        con = ql.connect("AddressBook.db")  # подключение к БД

        try:
            cur = con.cursor()  # открыла курсор к БД
            cur.execute("select * from address_book")  # выполнение запроса к БД на выборку данных
            recs = cur.fetchall()  # сохранение результата выборки в список

            self.twBook.clear()  # очистка виджета-списка

            colsWidth = (0, 120, 130, 120, 200)  # картеж ширины столбцов
            for i in range(5):
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
        self.f_add.leId.setText('')
        self.f_add.leName.setText('')
        self.f_add.leFamily.setText('')
        self.f_add.lePhone.setText('')
        self.f_add.leMail.setText('')
        self.f_add.leNote.setText('')
        self.f_add.show()

    def ev_sel(self):
        sel_items = self.twBook.selectedItems()
        if len(sel_items):
            self.acUpd.setEnabled(True)
            self.acDel.setEnabled(True)
        else:
            self.acUpd.setEnabled(False)
            self.acDel.setEnabled(False)

    def ev_upd(self):
        sel_items = self.twBook.selectedItems()
        if len(sel_items):
            self.ad.sel_item = sel_items[0]
            self.ad.leId.setText(self.ad.sel_item.text(0))
            self.ad.leName.setText(self.ad.sel_item.text(1))
            self.ad.leFamily.setText(self.ad.sel_item.text(2))
            self.ad.lePhone.setText(self.ad.sel_item.text(3))
            self.ad.leMail.setText(self.ad.sel_item.text(4))
            self.ad.leNote.setText(self.ad.sel_item.text(5))
            self.ad.show()

    def ev_del(self):
        sel_items = self.twBook.selectedItems()
        con = ql.connect("AddressBook.db")  # подключение к БД
        try:
            cur = con.cursor()  # открыла курсор к БД
            for sel_item in sel_items:
                cur.execute(f"delete from address_book where id={sel_item.text(0)}")
                self.twBook.takeTopLevelItem(self.twBook.indexOfTopLevelItem(sel_item))
            con.commit()
            cur.close()

        except ql.Error as er:  # если возникла ошибка
            self.sbMainForm.showMessage('Ошибка при подключении к БД: {0}'.format(er))  # вывести ошибку в статусе-формы
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД


class TfmCh(qw.QDialog):  # создание класса TfmCh от класса QMainWindow
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
        uic.loadUi("fmCh.ui", self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.pbOk.clicked.connect(self.ev_save)
        self.sel_item = qw.QTreeWidgetItem()

    def ev_save(self):
        con = ql.connect("AddressBook.db")
        try:
            cur = con.cursor()
            cur.execute(f'update address_book set '
                        f'name="{self.leName.text()}", '
                        f'fio="{self.leFamily.text()}", '
                        f'phone="{self.lePhone.text()}", '
                        f'mail="{self.leMail.text()}", '
                        f'note="{self.leNote.text()}" '
                        f'where id={self.leId.text()}')
            con.commit()
            cur.close()

        except ql.Error as er:  # если возникла ошибка
            self.sbMainForm.showMessage('Ошибка при подключении к БД: {0}'.format(er))  # вывести ошибку в статусе-формы
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД

        self.sel_item.setText(1, self.leName.text())
        self.sel_item.setText(2, self.leFamily.text())
        self.sel_item.setText(3, self.lePhone.text())
        self.sel_item.setText(4, self.leMail.text())
        self.sel_item.setText(5, self.leNote.text())

        self.close()


class TfmAdd(qw.QDialog):  # создание класса TfmCh от класса QMainWindow
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
        uic.loadUi("fmCh.ui", self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.pbOk.clicked.connect(self.ev_save)
        self.tv = qw.QTreeWidget()

    def ev_save(self):
        con = ql.connect("AddressBook.db")
        try:
            cur = con.cursor()
            item = (self.leName.text(),
                    self.leFamily.text(),
                    self.lePhone.text(),
                    self.leMail.text(),
                    self.leNote.text())

            cur.execute(f'insert into address_book (name,fio,phone,mail,note) values (?, ?, ?, ?, ?)', item)
            cur.execute('select seq from sqlite_sequence where name="address_book"')
            recs = cur.fetchall()  # сохранение результата выборки в список
            con.commit()
            cur.close()
            if len(recs):
                item = (recs[0][0],) + item
                qw.QTreeWidgetItem(self.tv, map(str, item))

        except ql.Error as er:  # если возникла ошибка
            self.sbMainForm.showMessage('Ошибка при подключении к БД: {0}'.format(er))  # вывести ошибку в статусе-формы
            print("Ошибка при подключении к БД", er)  # вывести в консоль ошибку

        finally:  # выполняется не взирая на ошибки
            con.close()  # отключение от БД

        self.close()


def main():
    app = qw.QApplication(sys.argv)  # Создаю объект, который управляет GUI, на основе класса QApplication
    ab = TABook()  # Создаю объект класса TABook
    print(ab.ad.pbOk.__dict__)
    ab.show()  # Показываю окно
    app.exec_()  # Запускаю обработку событий в нашем окне


if __name__ == '__main__':  # Если запускается файл напрямую, а не импортируется
    main()  # то запускается функция main()
