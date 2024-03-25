import csv
import random

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from About import Ui_About
from Definitions import Ui_Definitions
from MainWindow import Ui_MainWindow
from Open_Type import Ui_Open_Type
from Pictures import Ui_Pictures
from Settings import Ui_SettingsWindow
from Set_Creator_Director import Ui_Set_Creator_Director  # Importiere alle neuen UI-Dateien
from Set_Creator_T2T import Ui_Set_Creator_T2T  # für späteres Nutzen, Verknüpfung mit
from Set_Creator_T2I import Ui_Set_Creator_T2I  # den passenden Buttons muss noch gemacht
from Set_Creator_LText import Ui_Set_Creator_LText  # werden, Versuche ich noch zu machen (22.03. 9:13)

def_button_is_clicked = None
term_button_is_clicked = None
def_name_number = None
term_name_number = None
pictures_term_button_is_clicked = None
pictures_pic_button_is_clicked = None
pictures_term_name_number = None
pictures_pic_name_number = None
set_name = ""
correct_counter = 0
data = None


# Open Settings on Settings Button press
def settings_open():
    settings.show()
    pass


# Open About on About Button press
def about_open():
    about.show()
    pass


def open_type_open():
    open_type.show()
    pass


def set_creator_director_open():
    set_creator_director.show()
    pass


def set_creator_t2t_open():
    set_creator_t2t.show()
    pass


def set_creator_t2i_open():
    set_creator_t2i.show()
    pass


def set_creator_ltext_open():
    set_creator_ltext.show()
    pass


# Set selection on Open Set Button press
def definitions_open():
    global set_name
    # File Dialog for Set Select
    set_name = str(QFileDialog.getExistingDirectory(open_type, "Select Directory", "sets"))
    definitions_init()  # Call Innit Function


def pictures_open():
    global set_name
    # File Dialog for Set Select
    set_name = str(QFileDialog.getExistingDirectory(open_type, "Select Directory", "sets"))
    pictures_init()  # Call Innit Function


def pictures_init():
    global set_name  # Selected Set from definitions_open()
    global data
    data = csv_to_lists(set_name + "/pic1.csv")  # Call CSV function (see below)
    items = list(range(0, len(data)))  # Index of all Elements from data
    shuffle = [0, 1, 2]  # Shuffle-List for 2nd assignment
    random.shuffle(items)  # Shuffling both lists for randomness
    random.shuffle(shuffle)

    # Assign first 3 Items(Definitions) from Index to buttons
    def1 = items[0]
    def2 = items[1]
    def3 = items[2]

    # Assign the 3 corresponding shuffled Items(Terms)
    pic1 = items[shuffle[0]]
    pic2 = items[shuffle[1]]
    pic3 = items[shuffle[2]]

    pictures_ui.term1_button.setText(data[def1][0])  # Assigning chosen text to Buttons
    pictures_ui.term1_button.setToolTip(str(def1))  # Assigning Index as Tooltip for later use
    pictures_ui.term1_button.setVisible(True)  # In case of refresh
    pictures_ui.term1_button.setChecked(False)  # In case of refresh
    pictures_ui.pic1_button.setIcon(QIcon(set_name + "/pics/" + str(data[pic1][1]) + ".jpg"))  # Assign Pics
    pictures_ui.pic1_button.setToolTip(str(pic1))
    pictures_ui.pic1_button.setVisible(True)
    pictures_ui.pic1_button.setChecked(False)
    pictures_ui.term2_button.setText(data[def2][0])
    pictures_ui.term2_button.setToolTip(str(def2))
    pictures_ui.term2_button.setVisible(True)
    pictures_ui.term2_button.setChecked(False)
    pictures_ui.pic2_button.setIcon(QIcon(set_name + "/pics/" + str(data[pic2][1]) + ".jpg"))
    pictures_ui.pic2_button.setToolTip(str(pic2))
    pictures_ui.pic2_button.setVisible(True)
    pictures_ui.pic2_button.setChecked(False)
    pictures_ui.term3_button.setText(data[def3][0])
    pictures_ui.term3_button.setToolTip(str(def3))
    pictures_ui.term3_button.setVisible(True)
    pictures_ui.term3_button.setChecked(False)
    pictures_ui.pic3_button.setIcon(QIcon(set_name + "/pics/" + str(data[pic3][1]) + ".jpg"))
    pictures_ui.pic3_button.setToolTip(str(pic3))
    pictures_ui.pic3_button.setVisible(True)
    pictures_ui.pic3_button.setChecked(False)

    pictures.show()  # Show Window
    pass


def pictures_pic_button_clicked(index, number):
    global pictures_term_button_is_clicked
    global pictures_pic_button_is_clicked
    global pictures_term_name_number
    global pictures_pic_name_number
    global correct_counter
    pictures_pic_button_is_clicked = index
    pictures_pic_name_number = number

    if pictures_term_button_is_clicked is not None:
        if pictures_term_button_is_clicked == pictures_pic_button_is_clicked:
            pictures_term_button_is_clicked = None
            pictures_pic_button_is_clicked = None
            getattr(pictures_ui, "term" + str(pictures_term_name_number) + "_button").setVisible(False)
            getattr(pictures_ui, "pic" + str(pictures_pic_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1
            if correct_counter == 3:
                pictures_init()
                correct_counter = 0
        else:
            pictures_term_button_is_clicked = None
            pictures_pic_button_is_clicked = None
            getattr(pictures_ui, "term" + str(pictures_term_name_number) + "_button").setChecked(False)
            getattr(pictures_ui, "pic" + str(pictures_pic_name_number) + "_button").setChecked(False)
    pass


def pictures_term_button_clicked(index, number):
    global pictures_term_button_is_clicked  # Set-Index of last pressed Term-Button parsed as ToolTip
    global pictures_pic_button_is_clicked  # Set-Index of last pressed Def-Button parsed as ToolTip
    global pictures_term_name_number  # Number in Term-Button Name
    global pictures_pic_name_number  # Number in Def-Button Name
    global correct_counter  # Counter for refresh trigger
    pictures_term_button_is_clicked = index  # Assign parsed Index to var
    pictures_term_name_number = number  # Assign Name Number

    if pictures_pic_button_is_clicked is not None:  # If this is the second click
        if pictures_term_button_is_clicked == pictures_pic_button_is_clicked:  # If both buttons have the same Index
            # (are corresponding)
            pictures_term_button_is_clicked = None  # Reset Index Vars
            pictures_pic_button_is_clicked = None
            getattr(pictures_ui, "term" + str(pictures_term_name_number) + "_button").setVisible(False)  # Hiding
            # Buttons
            # for User Feedback
            getattr(pictures_ui, "pic" + str(pictures_pic_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1  # Counter Count-Up
            if correct_counter == 3:  # Check if time for refresh
                pictures_init()  # Run Refresh function
                correct_counter = 0  # Reset counter
        else:  # If not corresponding
            pictures_term_button_is_clicked = None  # Reset so no false checks happen
            pictures_pic_button_is_clicked = None
            getattr(pictures_ui, "term" + str(pictures_term_name_number) + "_button").setChecked(False)  # QOL reset
            getattr(pictures_ui, "pic" + str(pictures_pic_name_number) + "_button").setChecked(False)
    pass


# Innit on Set Select/Refresh on new Round for Definitions
def definitions_init():
    global set_name  # Selected Set from definitions_open()
    global data
    data = csv_to_lists(set_name + "/def1.csv")  # Call CSV function (see below)
    items = list(range(0, len(data)))  # Index of all Elements from data
    shuffle = [0, 1, 2]  # Shuffle-List for 2nd assignment
    random.shuffle(items)  # Shuffling both lists for randomness
    random.shuffle(shuffle)

    # Assign first 3 Items(Definitions) from Index to buttons
    def1 = items[0]
    def2 = items[1]
    def3 = items[2]

    # Assign the 3 corresponding shuffled Items(Terms)
    term1 = items[shuffle[0]]
    term2 = items[shuffle[1]]
    term3 = items[shuffle[2]]

    definitions_ui.def1_button.setText(data[def1][0])  # Assigning chosen text to Buttons
    definitions_ui.def1_button.setToolTip(str(def1))  # Assigning Index as Tooltip for later use
    definitions_ui.def1_button.setVisible(True)  # In case of refresh
    definitions_ui.def1_button.setChecked(False)  # In case of refresh
    definitions_ui.term1_button.setText(data[term1][1])
    definitions_ui.term1_button.setToolTip(str(term1))
    definitions_ui.term1_button.setVisible(True)
    definitions_ui.term1_button.setChecked(False)
    definitions_ui.def2_button.setText(data[def2][0])
    definitions_ui.def2_button.setToolTip(str(def2))
    definitions_ui.def2_button.setVisible(True)
    definitions_ui.def2_button.setChecked(False)
    definitions_ui.term2_button.setText(data[term2][1])
    definitions_ui.term2_button.setToolTip(str(term2))
    definitions_ui.term2_button.setVisible(True)
    definitions_ui.term2_button.setChecked(False)
    definitions_ui.def3_button.setText(data[def3][0])
    definitions_ui.def3_button.setToolTip(str(def3))
    definitions_ui.def3_button.setVisible(True)
    definitions_ui.def3_button.setChecked(False)
    definitions_ui.term3_button.setText(data[term3][1])
    definitions_ui.term3_button.setToolTip(str(term3))
    definitions_ui.term3_button.setVisible(True)
    definitions_ui.term3_button.setChecked(False)

    definitions.show()  # Show Window
    pass


# Checks on Button clicked (see below)
def definitions_def_button_clicked(index, number):
    global term_button_is_clicked
    global def_button_is_clicked
    global term_name_number
    global def_name_number
    global correct_counter
    def_button_is_clicked = index
    def_name_number = number

    if term_button_is_clicked is not None:
        if term_button_is_clicked == def_button_is_clicked:
            term_button_is_clicked = None
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setVisible(False)
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1
            if correct_counter == 3:
                definitions_init()
                correct_counter = 0
        else:
            term_button_is_clicked = None
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setChecked(False)
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setChecked(False)
    pass


def definition_term_button_clicked(index, number):
    global term_button_is_clicked  # Set-Index of last pressed Term-Button parsed as ToolTip
    global def_button_is_clicked  # Set-Index of last pressed Def-Button parsed as ToolTip
    global term_name_number  # Number in Term-Button Name
    global def_name_number  # Number in Def-Button Name
    global correct_counter  # Counter for refresh trigger
    term_button_is_clicked = index  # Assign parsed Index to var
    term_name_number = number  # Assign Name Number

    if def_button_is_clicked is not None:  # If this is the second click
        if term_button_is_clicked == def_button_is_clicked:  # If both buttons have the same Index (are corresponding)
            term_button_is_clicked = None  # Reset Index Vars
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setVisible(False)  # Hiding Buttons
            # for User Feedback
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1  # Counter Count-Up
            if correct_counter == 3:  # Check if time for refresh
                definitions_init()  # Run Refresh function
                correct_counter = 0  # Reset counter
        else:  # If not corresponding
            term_button_is_clicked = None  # Reset so no false checks happen
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setChecked(False)  # QOL reset
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setChecked(False)
    pass


def csv_to_lists(file_path):
    with open(file_path, newline='', encoding="utf-8") as csv_file:  # magic library things (encoding for umlaute)
        reader = csv.reader(csv_file, delimiter=";")
        rows = list(reader)
    return rows


app = QApplication([])
window = QMainWindow()
settings = QWidget()
about = QWidget()
open_type = QWidget()
definitions = QWidget()
pictures = QWidget()
set_creator_director = QWidget()
set_creator_t2t = QWidget()
set_creator_t2i = QWidget()
set_creator_ltext = QWidget()

# Landingpage Setup
landingpage_ui = Ui_MainWindow()
landingpage_ui.setupUi(window)
# Settings Setup
settings_ui = Ui_SettingsWindow()
settings_ui.setupUi(settings)
# About Setup
about_ui = Ui_About()
about_ui.setupUi(about)
# Open Type Select Setup
open_type_ui = Ui_Open_Type()
open_type_ui.setupUi(open_type)
# Definitions Setup
definitions_ui = Ui_Definitions()
definitions_ui.setupUi(definitions)
# Pictures Setup
pictures_ui = Ui_Pictures()
pictures_ui.setupUi(pictures)
# Creator Director Setup
set_creator_director_ui = Ui_Set_Creator_Director()
set_creator_director_ui.setupUi(set_creator_director)
# Creator t2t Setup
set_creator_t2t_ui = Ui_Set_Creator_T2T()
set_creator_t2t_ui.setupUi(set_creator_t2t)
# Creator t2i Setup
set_creator_t2i_ui = Ui_Set_Creator_T2I()
set_creator_t2i_ui.setupUi(set_creator_t2i)
# Creator LText Setup
set_creator_ltext_ui = Ui_Set_Creator_LText()
set_creator_ltext_ui.setupUi(set_creator_ltext)

# Landingpage Connects
landingpage_ui.SettingsButton.clicked.connect(settings_open)
landingpage_ui.OpenButton.clicked.connect(open_type_open)
landingpage_ui.CreateButton.clicked.connect(set_creator_director_open)
# Settings Connects
settings_ui.about_button.clicked.connect(about_open)
# Open Type Select Connects
open_type_ui.T2T_Button.clicked.connect(definitions_open)
open_type_ui.P2T_Button.clicked.connect(pictures_open)
# open_type_ui.LText_Button.clicked.connect()
# Definitions Connects
definitions_ui.def1_button.clicked.connect(lambda: definitions_def_button_clicked(definitions_ui.def1_button.toolTip(), 1))
definitions_ui.def2_button.clicked.connect(lambda: definitions_def_button_clicked(definitions_ui.def2_button.toolTip(), 2))
definitions_ui.def3_button.clicked.connect(lambda: definitions_def_button_clicked(definitions_ui.def3_button.toolTip(), 3))
definitions_ui.term1_button.clicked.connect(lambda: definition_term_button_clicked(definitions_ui.term1_button.toolTip(), 1))
definitions_ui.term2_button.clicked.connect(lambda: definition_term_button_clicked(definitions_ui.term2_button.toolTip(), 2))
definitions_ui.term3_button.clicked.connect(lambda: definition_term_button_clicked(definitions_ui.term3_button.toolTip(), 3))
# Pictures Connects
pictures_ui.pic1_button.clicked.connect(lambda: pictures_pic_button_clicked(pictures_ui.pic1_button.toolTip(), 1))
pictures_ui.pic2_button.clicked.connect(lambda: pictures_pic_button_clicked(pictures_ui.pic2_button.toolTip(), 2))
pictures_ui.pic3_button.clicked.connect(lambda: pictures_pic_button_clicked(pictures_ui.pic3_button.toolTip(), 3))
pictures_ui.term1_button.clicked.connect(lambda: pictures_term_button_clicked(pictures_ui.term1_button.toolTip(), 1))
pictures_ui.term2_button.clicked.connect(lambda: pictures_term_button_clicked(pictures_ui.term2_button.toolTip(), 2))
pictures_ui.term3_button.clicked.connect(lambda: pictures_term_button_clicked(pictures_ui.term3_button.toolTip(), 3))

# Creator Director Contents
set_creator_director_ui.Add_T2T_Button.clicked.connect(set_creator_t2t_open)
set_creator_director_ui.Add_T2I_Button.clicked.connect(set_creator_t2i_open)
set_creator_director_ui.Add_LText_Button.clicked.connect(set_creator_ltext_open)


window.show()
app.exec()
