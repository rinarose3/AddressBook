# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmCh.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fmCh(object):
    def setupUi(self, fmCh):
        fmCh.setObjectName("fmCh")
        fmCh.resize(333, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fmCh.setWindowIcon(icon)
        fmCh.setWhatsThis("")
        fmCh.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(fmCh)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbName = QtWidgets.QLabel(fmCh)
        self.lbName.setObjectName("lbName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbName)
        self.lbFamily = QtWidgets.QLabel(fmCh)
        self.lbFamily.setObjectName("lbFamily")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbFamily)
        self.leFamily = QtWidgets.QLineEdit(fmCh)
        self.leFamily.setObjectName("leFamily")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leFamily)
        self.lbPhone = QtWidgets.QLabel(fmCh)
        self.lbPhone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbPhone.setObjectName("lbPhone")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbPhone)
        self.lePhone = QtWidgets.QLineEdit(fmCh)
        self.lePhone.setObjectName("lePhone")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.lbMail = QtWidgets.QLabel(fmCh)
        self.lbMail.setObjectName("lbMail")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbMail)
        self.leMail = QtWidgets.QLineEdit(fmCh)
        self.leMail.setObjectName("leMail")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leMail)
        self.lbNotes = QtWidgets.QLabel(fmCh)
        self.lbNotes.setObjectName("lbNotes")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbNotes)
        self.leNote = QtWidgets.QLineEdit(fmCh)
        self.leNote.setObjectName("leNote")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.leNote)
        self.leName = QtWidgets.QLineEdit(fmCh)
        self.leName.setText("")
        self.leName.setObjectName("leName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leName)
        self.label = QtWidgets.QLabel(fmCh)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leId = QtWidgets.QLineEdit(fmCh)
        self.leId.setEnabled(False)
        self.leId.setObjectName("leId")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leId)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pbOk = QtWidgets.QPushButton(fmCh)
        self.pbOk.setObjectName("pbOk")
        self.horizontalLayout_8.addWidget(self.pbOk)
        self.pbCansel = QtWidgets.QPushButton(fmCh)
        self.pbCansel.setObjectName("pbCansel")
        self.horizontalLayout_8.addWidget(self.pbCansel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.retranslateUi(fmCh)
        self.pbCansel.clicked.connect(fmCh.close)
        QtCore.QMetaObject.connectSlotsByName(fmCh)
        fmCh.setTabOrder(self.leName, self.leFamily)
        fmCh.setTabOrder(self.leFamily, self.lePhone)
        fmCh.setTabOrder(self.lePhone, self.leMail)
        fmCh.setTabOrder(self.leMail, self.leNote)
        fmCh.setTabOrder(self.leNote, self.pbOk)
        fmCh.setTabOrder(self.pbOk, self.pbCansel)
        fmCh.setTabOrder(self.pbCansel, self.leId)

    def retranslateUi(self, fmCh):
        _translate = QtCore.QCoreApplication.translate
        fmCh.setWindowTitle(_translate("fmCh", "Dialog"))
        self.lbName.setText(_translate("fmCh", "Имя"))
        self.lbFamily.setText(_translate("fmCh", "Фамилия"))
        self.lbPhone.setText(_translate("fmCh", "Телефон"))
        self.lbMail.setText(_translate("fmCh", "e_mail"))
        self.lbNotes.setText(_translate("fmCh", "Заметки"))
        self.label.setText(_translate("fmCh", "id"))
        self.pbOk.setText(_translate("fmCh", "ОК"))
        self.pbCansel.setText(_translate("fmCh", "Отмена"))
