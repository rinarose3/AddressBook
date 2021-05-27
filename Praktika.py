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

        self.acAdd.triggered.connect(self.ev_add)  # связывание сигнала действия-добавления с моим слотом
        self.twBook.itemSelectionChanged.connect(self.ev_sel)
        self.acUpd.triggered.connect(self.ev_upd)

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
        self.ad.show()

    def ev_sel(self):
        sel_items = self.twBook.selectedItems()
        if len(sel_items):
            self.acUpd.setEnabled(True)
            self.acDel.setEnabled(True)
        else:
            self.acUpd.setEnabled(False)
            self.acDel.setEnabled(False)
#        for item in sel_items:

    def ev_upd(self):
        sel_items = self.twBook.selectedItems()
        if len(sel_items):
            sel_item = sel_items[0]
            self.ad.leName.setText(sel_item.text(1))
            self.ad.leFamily.setText(sel_item.text(2))
            self.ad.lePhone.setText(sel_item.text(3))
            self.ad.leMail.setText(sel_item.text(4))
            self.ad.leNote.setText(sel_item.text(5))
            self.ad.show()


class TfmCh(qw.QDialog):  # создание класса TfmCh от класса QMainWindow
    def __init__(self):  # конструктор моего класса
        super().__init__()  # вызов конструктора родителя
        uic.loadUi("fmCh.ui", self)  # конвертация разметки формы (ui) в поля и методы моего класса
        self.pbOk.clicked.connect(self.ev_save)

    def ev_save(self):
        print("Нажали кнопку")
        print("Проверка комита")


def main():
    app = qw.QApplication(sys.argv)  # Создаю объект, который управляет GUI, на основе класса QApplication
    ab = TABook()  # Создаю объект класса TABook
    ab.show()  # Показываю окно
    app.exec_()  # Запускаю обработку событий в нашем окне


if __name__ == '__main__':  # Если запускается файл напрямую, а не импортируется
    main()  # то запускается функция main()
