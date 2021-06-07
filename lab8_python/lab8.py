from PyQt5 import QtWidgets, uic
from mainwindow import Ui_MainWindow
from login_screen import Ui_login_window
from errorbox import Ui_errorbox
from messagebox import Ui_messagebox
from contract_insert import Ui_contract_insert
from supplier_insert import Ui_supplier_insert
from product_insert import Ui_product_insert
from supplier_update import Ui_supplier_update
from contract_update import Ui_contract_update
from product_update import Ui_product_update
from contract_delete import Ui_contract_delete
from supplier_delete import Ui_supplier_delete
from product_delete import Ui_product_delete
from tables import Ui_ShowDB
from first_proced import Ui_first_proced
from first_proced_show import Ui_first_proced_show
from legal_insert import Ui_legal_insert
from private_insert import Ui_private_insert
from legal_delete import Ui_legal_delete
from private_delete import Ui_private_delete
import sys
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector
from mysql.connector import Error
import datetime

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

class message_box(QtWidgets.QDialog):
    def __init__(self):
        super(message_box, self).__init__()
        self.ui = Ui_messagebox()
        self.ui.setupUi(self)

class error_box(QtWidgets.QDialog):
    def __init__(self):
        super(error_box, self).__init__()
        self.ui = Ui_errorbox()
        self.ui.setupUi(self)

class mywindow(QtWidgets.QMainWindow):
    connection = create_connection("localhost", "root", "", "delivery")
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_login_screen.triggered.connect(self.login_button_clicked)
        self.ui.pushButton_contract_insert.clicked.connect(self.contract_insert_clicked)
        self.ui.pushButton_supplier_insert.clicked.connect(self.supplier_insert_clicked)
        self.ui.pushButton_product_insert.clicked.connect(self.product_insert_clicked)
        self.ui.pushButton_supplier_update.clicked.connect(self.supplier_update_clicked)
        self.ui.pushButton_contract_update.clicked.connect(self.contract_update_clicked)
        self.ui.pushButton_product_update.clicked.connect(self.product_update_clicked)
        self.ui.pushButton_contract_delete.clicked.connect(self.contract_delete_clicked)
        self.ui.pushButton_supplier_delete.clicked.connect(self.supplier_delete_clicked)
        self.ui.pushButton_product_delete.clicked.connect(self.product_delete_clicked)
        self.ui.show_db.triggered.connect(self.show_db)
        self.ui.open_procedure_1.triggered.connect(self.proced_1)
        self.ui.pushButton_legal_insert.clicked.connect(self.legal_insert_clicked)
        self.ui.pushButton_private_insert.clicked.connect(self.private_insert_clicked)
        self.ui.pushButton_legal_delete.clicked.connect(self.legal_delete_clicked)
        self.ui.pushButton_private_delete.clicked.connect(self.private_delete_clicked)


    def legal_insert_clicked(self):
        self.w2 = legal_insert_window()
        self.w2.exec()

    def private_insert_clicked(self):
        self.w2 = private_insert_window()
        self.w2.exec()

    def legal_delete_clicked(self):
        self.w2 = legal_delete_window()
        self.w2.exec()

    def private_delete_clicked(self):
        self.w2 = private_delete_window()
        self.w2.exec()

    def proced_1(self):
        self.w2 = show_first_procedure()
        self.w2.exec()

    def show_db(self):
        self.w2 = show_window()
        self.w2.exec()

    def login_button_clicked(self):
        self.w2 = login_window()
        self.w2.exec()

    def contract_delete_clicked(self):
        self.w2 = contract_delete_window()
        self.w2.exec()

    def supplier_delete_clicked(self):
        self.w2 = supplier_delete_window()
        self.w2.exec()

    def product_delete_clicked(self):
        self.w2 = product_delete_window()
        self.w2.exec()

    def contract_insert_clicked(self):
        self.w2 = contract_insert_window()
        self.w2.exec()

    def supplier_insert_clicked(self):
        self.w2 = supplier_insert_window()
        self.w2.exec()

    def product_insert_clicked(self):
        self.w2 = product_insert_window()
        self.w2.exec()

    def supplier_update_clicked(self):
        self.w2 = supplier_update_window()
        self.w2.exec()

    def contract_update_clicked(self):
        self.w2 = contract_update_window()
        self.w2.exec()

    def product_update_clicked(self):
        self.w2 = product_update_window()
        self.w2.exec()

class show_window(QtWidgets.QDialog):
    def __init__(self):
        super(show_window, self).__init__()
        self.ui = Ui_ShowDB()
        self.ui.setupUi(self)

        cursor = application.connection.cursor()
        select_supplier = None
        cursor.execute("SELECT * FROM supplier")
        select_supplier = cursor.fetchall()
        print(select_supplier)

        for i in range(0, len(select_supplier)):
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            for j in range(0, 3):
                a = QTableWidgetItem(str(select_supplier[i][j]))
                self.ui.tableWidget.setItem(i, j, a)

        application.connection.commit()

        cursor = application.connection.cursor()
        select_contract = None
        cursor.execute("SELECT * FROM contract")
        select_contract = cursor.fetchall()

        for i in range(0, len(select_contract)):
            self.ui.tableWidget_2.setRowCount(self.ui.tableWidget_2.rowCount() + 1)
            for j in range(0, 5):
                a = QTableWidgetItem(str(select_contract[i][j]))
                self.ui.tableWidget_2.setItem(i, j, a)
        application.connection.commit()

        cursor = application.connection.cursor()
        select_product = None
        cursor.execute("SELECT * FROM product")
        select_product = cursor.fetchall()

        for i in range(0, len(select_product)):
            self.ui.tableWidget_3.setRowCount(self.ui.tableWidget_3.rowCount() + 1)
            for j in range(0, 4):
                a = QTableWidgetItem(str(select_product[i][j]))
                self.ui.tableWidget_3.setItem(i, j, a)

        application.connection.commit()

        cursor = application.connection.cursor()
        select_legal = None
        cursor.execute("SELECT * FROM legal_supplier")
        select_legal = cursor.fetchall()

        for i in range(0, len(select_legal)):
            self.ui.tableWidget_4.setRowCount(self.ui.tableWidget_4.rowCount() + 1)
            for j in range(0, 3):
                a = QTableWidgetItem(str(select_legal[i][j]))
                self.ui.tableWidget_4.setItem(i, j, a)

        application.connection.commit()

        cursor = application.connection.cursor()
        select_private = None
        cursor.execute("SELECT * FROM private_supplier")
        select_private = cursor.fetchall()

        for i in range(0, len(select_private)):
            self.ui.tableWidget_5.setRowCount(self.ui.tableWidget_5.rowCount() + 1)
            for j in range(0, 5):
                a = QTableWidgetItem(str(select_private[i][j]))
                self.ui.tableWidget_5.setItem(i, j, a)

        application.connection.commit()


class show_first_procedure(QtWidgets.QDialog):

    def __init__(self):
        super(show_first_procedure, self).__init__()
        self.ui = Ui_first_proced()
        self.ui.setupUi(self)
        self.ui.pushButton_create_report.clicked.connect(self.btnCreate)

    def btnCreate(self):
        global b
        b = self.ui.lineEdit.text()
        self.w2 = show_first_procedure_2()
        self.w2.exec()

class show_first_procedure_2(QtWidgets.QDialog):
    def __init__(self):
        super(show_first_procedure_2, self).__init__()
        self.ui = Ui_first_proced_show()
        self.ui.setupUi(self)
        try:
            cursor = application.connection.cursor()
            global b

            a = [int(b)]
            report_result = None
            cursor.callproc('GetListOfSuppliedProductsByNumber', a)

            for result in cursor.stored_results():
                report_result = result.fetchall()

            print(report_result)

            for i in range(0, len(report_result)):
                self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
                for j in range(0, 3):
                    a = QTableWidgetItem(str(report_result[i][j]))
                    self.ui.tableWidget.setItem(i, j, a)

            application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()


class supplier_insert_window(QtWidgets.QDialog):
    def __init__(self):
        super(supplier_insert_window, self).__init__()
        self.ui = Ui_supplier_insert()
        self.ui.setupUi(self)
        self.ui.pushButton_supplier_insert.clicked.connect(self.btnInsert)

    def btnInsert(self):
        try:
            id = self.ui.lineEdit_supplier_id.text()
            name = self.ui.lineEdit_supplier_name.text()
            address = self.ui.lineEdit_supplier_address.text()

            with application.connection.cursor() as cursor:
                kor1 = (int(id), name, address)
                cursor.execute("INSERT INTO supplier VALUES (%s,%s,%s)", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class contract_insert_window(QtWidgets.QDialog):
    def __init__(self):
        super(contract_insert_window, self).__init__()
        self.ui = Ui_contract_insert()
        self.ui.setupUi(self)
        self.ui.pushButton_contract_insert.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_contract_id.text()
            supplier = self.ui.lineEdit_contract_supplier.text()
            title = self.ui.lineEdit_contract_title.text()
            note = self.ui.lineEdit_contract_note.text()

            with application.connection.cursor() as cursor:
                kor1 = (int(id), datetime.datetime.now(), int(supplier), title, note)
                cursor.execute("INSERT INTO contract VALUES (%s,%s,%s,%s,%s)", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class product_insert_window(QtWidgets.QDialog):
    def __init__(self):
        super(product_insert_window, self).__init__()
        self.ui = Ui_product_insert()
        self.ui.setupUi(self)
        self.ui.pushButton_product_insert.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            contract = self.ui.lineEdit_product_contract.text()
            name = self.ui.lineEdit_product_name.text()
            amount = self.ui.lineEdit_product_amount.text()
            price = self.ui.lineEdit_product_price.text()

            with application.connection.cursor() as cursor:
                kor1 = (int(contract), name, int(amount), float(price))
                cursor.execute("INSERT INTO product VALUES (%s,%s,%s,%s)", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class supplier_update_window(QtWidgets.QDialog):
    def __init__(self):
        super(supplier_update_window, self).__init__()
        self.ui = Ui_supplier_update()
        self.ui.setupUi(self)
        self.ui.pushButton_supplier_update.clicked.connect(self.btnInsert)

    def btnInsert(self):
        try:
            id = self.ui.lineEdit_supplier_id.text()
            name = self.ui.lineEdit_supplier_name.text()
            address = self.ui.lineEdit_supplier_address.text()

            with application.connection.cursor() as cursor:
                kor1 = (name, address, int(id))
                cursor.execute("UPDATE supplier SET name = %s, address = %s WHERE id = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class contract_update_window(QtWidgets.QDialog):
    def __init__(self):
        super(contract_update_window, self).__init__()
        self.ui = Ui_contract_update()
        self.ui.setupUi(self)
        self.ui.pushButton_contract_update.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_contract_id.text()
            supplier = self.ui.lineEdit_contract_supplier.text()
            title = self.ui.lineEdit_contract_title.text()
            note = self.ui.lineEdit_contract_note.text()

            with application.connection.cursor() as cursor:
                kor1 = (title, note, int(id))
                cursor.execute("UPDATE contract SET title = %s, note = %s WHERE number = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class product_update_window(QtWidgets.QDialog):
    def __init__(self):
        super(product_update_window, self).__init__()
        self.ui = Ui_product_update()
        self.ui.setupUi(self)
        self.ui.pushButton_product_insert.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            contract = self.ui.lineEdit_product_contract.text()
            name = self.ui.lineEdit_product_name.text()
            amount = self.ui.lineEdit_product_amount.text()
            price = self.ui.lineEdit_product_price.text()

            with application.connection.cursor() as cursor:
                kor1 = (int(amount), float(price), name)
                cursor.execute("UPDATE product SET amount = %s, price = %s WHERE product = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class supplier_delete_window(QtWidgets.QDialog):
    def __init__(self):
        super(supplier_delete_window, self).__init__()
        self.ui = Ui_supplier_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_supplier_delete.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_supplier.text()
            print(id)

            with application.connection.cursor() as cursor:
                kor1 = (int(id),)
                cursor.execute("DELETE FROM supplier WHERE id = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class contract_delete_window(QtWidgets.QDialog):
    def __init__(self):
        super(contract_delete_window, self).__init__()
        self.ui = Ui_contract_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_contract_delete.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            number = self.ui.lineEdit_contract.text()

            cursor = application.connection.cursor()

            kor1 = (int(number),)
            cursor.execute("DELETE FROM contract WHERE number = %s", kor1)
            application.connection.commit()


        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class product_delete_window(QtWidgets.QDialog):
    def __init__(self):
        super(product_delete_window, self).__init__()
        self.ui = Ui_product_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_product_delete.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_product.text()

            with application.connection.cursor() as cursor:
                kor1 = (id,)
                cursor.execute("DELETE FROM product WHERE product.product = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class login_window(QtWidgets.QDialog):
    def __init__(self):
        super(login_window, self).__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.ui.pushButton_login_commit.clicked.connect(self.btnInsert)

    def btnInsert(self):
        try:
            login = self.ui.login_line.text()
            password = self.ui.password_line.text()
            if (login == "root" and password == ""):
                application.connection = create_connection("localhost", login, password, "delivery")
                self.close()
            elif(login == "supply_manag" and password == "12345"):
                application.connection = create_connection("localhost", login, password, "delivery")
                self.close()
            elif(login == "accountant" and password == "supply"):
                application.connection = create_connection("localhost", login, password, "delivery")
                self.close()
            elif(login == "market_manag" and password == "supply"):
                application.connection = create_connection("localhost", login, password, "delivery")
                self.close()
            else:
                self.w2 = error_box()
                self.w2.exec()
        except:
            self.w2 = error_box()
            self.w2.exec()

class legal_insert_window(QtWidgets.QDialog):
    def __init__(self):
        super(legal_insert_window, self).__init__()
        self.ui = Ui_legal_insert()
        self.ui.setupUi(self)
        self.ui.pushButton_legal_insert.clicked.connect(self.btnInsert_insert)
        self.ui.pushButton_legal_update.clicked.connect(self.btnInsert_update)

    def btnInsert_insert(self):
        try:
            id = self.ui.lineEdit_legal_id.text()
            tax = self.ui.lineEdit_legal_tax.text()
            vat = self.ui.lineEdit_legal_vat.text()
            if (tax.isdigit() and vat.isdigit()):
                with application.connection.cursor() as cursor:
                    vat = "UA" + vat
                    kor1 = (int(id), tax, vat)
                    cursor.execute("INSERT INTO legal_supplier VALUES (%s,%s,%s)", kor1)
                    application.connection.commit()

            else:
                raise Exception("Some exception")

        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

    def btnInsert_update(self):
        try:
            id = self.ui.lineEdit_legal_id.text()
            tax = self.ui.lineEdit_legal_tax.text()
            vat = self.ui.lineEdit_legal_vat.text()


            if (tax.isdigit() and vat.isdigit()):
                with application.connection.cursor() as cursor:
                    vat = "UA"+vat
                    kor1 = (tax, vat, int(id))
                    cursor.execute("UPDATE legal_supplier SET tax_number = %s, vat_number = %s WHERE id = %s", kor1)
                    application.connection.commit()

            else:
                raise Exception("Some exception")

        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class private_insert_window(QtWidgets.QDialog):
    def __init__(self):
        super(private_insert_window, self).__init__()
        self.ui = Ui_private_insert()
        self.ui.setupUi(self)
        self.ui.pushButton_private_insert.clicked.connect(self.btnInsert_insert)
        self.ui.pushButton_private_update.clicked.connect(self.btnInsert_update)

    def btnInsert_insert(self):
        try:
            id = self.ui.lineEdit_private_id.text()
            last = self.ui.lineEdit_private_last.text()
            first = self.ui.lineEdit_private_first.text()
            second = self.ui.lineEdit_private_second.text()
            number = self.ui.lineEdit_private_number.text()

            with application.connection.cursor() as cursor:
                kor1 = (int(id), last, first, second, number)
                cursor.execute("INSERT INTO private_supplier VALUES (%s,%s,%s,%s,%s)", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

    def btnInsert_update(self):
        try:
            id = self.ui.lineEdit_private_id.text()
            last = self.ui.lineEdit_private_last.text()
            first = self.ui.lineEdit_private_first.text()
            second = self.ui.lineEdit_private_second.text()
            number = self.ui.lineEdit_private_number.text()

            with application.connection.cursor() as cursor:
                kor1 = (last, first, second, number, int(id))
                cursor.execute("UPDATE private_supplier SET last_name = %s, first_name = %s, second_name = %s, reg_number = %s WHERE id = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class legal_delete_window(QtWidgets.QDialog):
    def __init__(self):
        super(legal_delete_window, self).__init__()
        self.ui = Ui_legal_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_legal_delete.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_legal.text()
            print(id)

            with application.connection.cursor() as cursor:
                kor1 = (int(id),)
                cursor.execute("DELETE FROM legal_supplier WHERE id = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

class private_delete_window(QtWidgets.QDialog):
    def __init__(self):
        super(private_delete_window, self).__init__()
        self.ui = Ui_private_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_private_delete.clicked.connect(self.btnInsert)
    def btnInsert(self):
        try:
            id = self.ui.lineEdit_private.text()
            print(id)

            with application.connection.cursor() as cursor:
                kor1 = (int(id),)
                cursor.execute("DELETE FROM private_supplier WHERE id = %s", kor1)
                application.connection.commit()
        except:
            self.w2 = error_box()
            self.w2.exec()
        else:
            self.w2 = message_box()
            self.w2.exec()

global b
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())