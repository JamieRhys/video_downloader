from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, \
    QFormLayout, QWidget

from entities.Video import Video


class AddVideoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Video")
        self.setMinimumWidth(500)

        self.video = Video()

        # Create layouts
        self.layout_root = QVBoxLayout()
        self.layout_video = QFormLayout()
        self.layout_flac = QFormLayout()

        # Generate Sections
        self.__generate_video_section()
        self.__generate_flac_section()
        self.__generate_button_section()

        # Set initial visibility based on the convert flag
        self.__on_convert_toggle()

        self.setLayout(self.layout_root)


# On Change Handlers

    def __on_url_change(self, value: str):
        self.video.url = value


    def __on_output_name__change(self, value: str):
        self.video.output_name = value


# On Click Handlers

    def __on_add_button_clicked(self):
        self.accept()


    def __on_cancel_button_clicked(self):
        self.reject()

# On Toggle Handlers

    def __on_convert_toggle(self):
        if self.cb_convert.isChecked():
            if self.layout_flac.count() == 0:
                self.__generate_flac_section()

            self.layout_root.insertLayout(self.layout_root.count() - 1, self.layout_flac)
        else:
            self.__remove_flac_section()

        self.video.convert = self.cb_convert.isChecked()

# Generation Methods

    def __generate_video_section(self):
        self.lbl_video = QLabel("Video Options:")

        self.le_url = QLineEdit()
        self.le_url.setPlaceholderText("URL")
        self.le_url.textChanged.connect(self.__on_url_change)

        self

        self.cb_convert = QCheckBox()
        self.cb_convert.setText("Convert to FLAC?")
        self.cb_convert.setChecked(self.video.convert)
        self.cb_convert.stateChanged.connect(self.__on_convert_toggle)

        self.layout_video.addRow(self.lbl_video)
        self.layout_video.addRow(self.le_url)
        self.layout_video.addRow(self.cb_convert)

        self.layout_root.addLayout(self.layout_video)


    def __generate_flac_section(self):
        self.lbl_flac = QLabel("FLAC Tags:")

        self.layout_flac.addRow(self.lbl_flac)


    def __generate_button_section(self):
        button_box = QDialogButtonBox()

        btn_add = QPushButton("Add")
        btn_add.clicked.connect(self.__on_add_button_clicked)
        button_box.addButton(btn_add, QDialogButtonBox.ButtonRole.AcceptRole)

        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.__on_cancel_button_clicked)
        button_box.addButton(btn_cancel, QDialogButtonBox.ButtonRole.RejectRole)

        self.layout_root.addWidget(button_box)


# Helper methods

    def __remove_flac_section(self):
        # Clear all widgets from layout_flac
        while self.layout_flac.count():
            item = self.layout_flac.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            elif item.layout():
                self.__remove_flac_section_from_parent(item.layout())

        # Optionally, if you want to remove the layout_flac from the parent layout
        if self.layout_root:
            self.layout_root.removeItem(self.layout_flac)

        # Destroy the layout if necessary
        self.layout_flac.deleteLater()


    def __remove_flac_section_from_parent(self, layout):
        # Recursively clear child layouts
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            elif item.layout():
                self.__remove_flac_section_from_parent(item.layout())
        layout.deleteLater()