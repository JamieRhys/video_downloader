from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, \
    QFormLayout, QWidget

from entities.Video import Video

# This dialog is responsible for allowing the user to add a video to be downloaded.
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

    # Called when the URL line edit is changed.
    def __on_url_change(self, value: str):
        self.video.url = value

    # Called when the output name line edit is changed.
    def __on_output_name__change(self, value: str):
        self.video.output_name = value


# On Click Handlers

    # Called when the Add Button is clicked. It passes a populated Video object to the
    # calling window.
    def __on_add_button_clicked(self):
        self.accept()


    # Called when the Cancel Button is pressed. This will remove all previously inputted information
    # and return to the previous window.
    def __on_cancel_button_clicked(self):
        self.reject()

# On Toggle Handlers

    # Called when the convert video checkbox is either checked or not.
    def __on_convert_toggle(self):
        # Check to see if the box is checked.
        if self.cb_convert.isChecked():
            # If it is, add the FLAC Tag section to the dialog.
            # Here, we need to check if the count is zero or not, if it is, we need to
            # rebuild the layout as it might have previously been removed.
            if self.layout_flac.count() == 0:
                self.__generate_flac_section()

            # Insert the layout just above the buttons layout, but below the video layout.
            self.layout_root.insertLayout(self.layout_root.count() - 1, self.layout_flac)
        else:
            # If it's not checked, we need to remove the FLAC questions as the user does not need
            # these.
            self.__remove_flac_section()

        # Add the outcome to our video object as we'll need this when actually running through the
        # download and potential conversion.
        self.video.convert = self.cb_convert.isChecked()


    def __on_delete_toggle(self):
        self.video.delete = self.cb_delete.isChecked()

# Generation Methods

    # Called in the init method, this will generate and build the video section
    # of the dialog. It is then added to the main root layout so it can be displayed
    # to the user.
    def __generate_video_section(self):
        self.lbl_video = QLabel("Video Options:")

        # URL Line Edit
        self.le_url = QLineEdit()
        self.le_url.setPlaceholderText("URL")
        self.le_url.textChanged.connect(self.__on_url_change)

        # Output Name Line Edit
        self.le_output_name = QLineEdit()
        self.le_output_name.setPlaceholderText("Video name (Leave blank to have original video name)")
        self.le_output_name.textChanged.connect(self.__on_output_name__change)

        # Convert Video Checkbox
        self.cb_convert = QCheckBox()
        self.cb_convert.setText("Convert to FLAC?")
        self.cb_convert.setChecked(self.video.convert)
        self.cb_convert.stateChanged.connect(self.__on_convert_toggle)

        # Delete Original Video Checkbox
        self.cb_delete = QCheckBox()
        self.cb_delete.setText("Delete original video? (Only works if converting to FLAC)")
        self.cb_delete.setChecked(self.video.delete)
        self.cb_delete.stateChanged.connect(self.__on_delete_toggle)

        # Add the above components to the video layout.
        self.layout_video.addRow(self.lbl_video)
        self.layout_video.addRow(self.le_url)
        self.layout_video.addRow(self.le_output_name)
        self.layout_video.addRow(self.cb_convert)
        self.layout_video.addRow(self.cb_delete)


        # Add to the root layout.
        self.layout_root.addLayout(self.layout_video)

    # Called both in the init method and the on_convert_changed method, this will
    # generate and build the FLAC section of the dialog. This will ask tag related questions
    # if the user wishes to utilise them.
    def __generate_flac_section(self):
        self.lbl_flac = QLabel("FLAC Tags:")

        self.layout_flac.addRow(self.lbl_flac)


    # Called in the init method, this will generate and build the Button Box section of the dialog
    # box. This then allows the user to either apply the new video or cancel it and go back to the
    # original main window.
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