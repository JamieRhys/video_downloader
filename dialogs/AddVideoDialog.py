from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, \
    QFormLayout, QWidget, QComboBox, QDateEdit, QHBoxLayout

from entities.FlacTags import FlacTags
from entities.Video import Video, VideoType


# This dialog is responsible for allowing the user to add a video to be downloaded.
class AddVideoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Video")
        self.setMinimumWidth(500)

        self.__video = Video()

        # Create layouts
        self.__layout_root = QVBoxLayout()
        self.__layout_video = QFormLayout()

        # Generate Sections
        self.__generate_video_section()
        self.__generate_flac_section()
        self.__generate_button_section()

        # Set initial visibility based on the convert flag
        self.__on_convert_toggle()

        self.setLayout(self.__layout_root)


# On Change Handlers

    # Called when the URL line edit is changed.
    def __on_url_change(self, value: str): self.__video.url = value


    # Called when the output name line edit is changed.
    def __on_output_name__change(self, value: str): self.__video.output_name = value


    def __on_video_type_change(self, value: int):
        if value == VideoType.Single:
            self.__video.video_type = VideoType.Single
        elif value == VideoType.PlayList:
            self.__video.video_type = VideoType.PlayList


    def __on_title_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.title = value

    def __on_artist_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.artist = value

    def __on_band_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.band = value

    def __on_album_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.album = value

    def __on_release_date_change(self, value: QDate):
        self.__init_flac_tags()
        self.__video.flac_tags.release_date = value.toString("yyyy-MM-dd")

    def __on_comment_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.comment = value

    def __on_copyright_change(self, value: str):
        self.__init_flac_tags()
        self.__video.flac_tags.copyright = value



# On Click Handlers

    # Called when the Add Button is clicked. It passes a populated Video object to the
    # calling window.
    def __on_add_button_clicked(self):
        print(self.__video)
        self.accept()


    # Called when the Cancel Button is pressed. This will remove all previously inputted information
    # and return to the previous window.
    def __on_cancel_button_clicked(self):
        self.reject()

# On Toggle Handlers

    # Called when the convert video checkbox is either checked or not.
    def __on_convert_toggle(self):
        # Check to see if the box is checked.
        if self.__cb_convert.isChecked():
            # If it is, add the FLAC Tag section to the dialog.
            # Here, we need to check if the count is zero or not, if it is, we need to
            # rebuild the layout as it might have previously been removed.
            self.__generate_flac_section()

            # Insert the layout just above the buttons layout, but below the video layout.
            self.__layout_root.insertLayout(self.__layout_root.count() - 1, self.__layout_flac)
        else:
            # If it's not checked, we need to remove the FLAC questions as the user does not need
            # these.
            self.__remove_flac_section()
            self.__layout_flac = None

        # Add the outcome to our video object as we'll need this when actually running through the
        # download and potential conversion.
        self.__video.convert = self.__cb_convert.isChecked()


    def __on_delete_toggle(self):
        self.__video.delete = self.__cb_delete.isChecked()

# Generation Methods

    # Called in the init method, this will generate and build the video section
    # of the dialog. It is then added to the main root layout so it can be displayed
    # to the user.
    def __generate_video_section(self):
        self.lbl_video = QLabel("Video Options:")

        # URL Line Edit
        self.__le_url = QLineEdit()
        self.__le_url.setPlaceholderText("URL")
        self.__le_url.textChanged.connect(self.__on_url_change)

        # Output Name Line Edit
        self.__le_output_name = QLineEdit()
        self.__le_output_name.setPlaceholderText("Video name (Leave blank to have original video name)")
        self.__le_output_name.textChanged.connect(self.__on_output_name__change)

        self.__cmb_video_type = QComboBox()
        self.__cmb_video_type.setPlaceholderText("Video type")
        self.__cmb_video_type.addItems(["Single", "Playlist"])
        self.__cmb_video_type.currentIndexChanged.connect(self.__on_video_type_change)

        # Convert Video Checkbox
        self.__cb_convert = QCheckBox()
        self.__cb_convert.setText("Convert to FLAC?")
        self.__cb_convert.setChecked(self.__video.convert)
        self.__cb_convert.stateChanged.connect(self.__on_convert_toggle)

        # Delete Original Video Checkbox
        self.__cb_delete = QCheckBox()
        self.__cb_delete.setText("Delete original video? (Only works if converting to FLAC)")
        self.__cb_delete.setChecked(self.__video.delete)
        self.__cb_delete.stateChanged.connect(self.__on_delete_toggle)

        # Add the above components to the video layout.
        self.__layout_video.addRow(self.lbl_video)
        self.__layout_video.addRow(self.__le_url)
        self.__layout_video.addRow(self.__le_output_name)
        self.__layout_video.addRow(self.__cmb_video_type)
        self.__layout_video.addRow(self.__cb_convert)
        self.__layout_video.addRow(self.__cb_delete)


        # Add to the root layout.
        self.__layout_root.addLayout(self.__layout_video)

    # Called both in the init method and the on_convert_changed method, this will
    # generate and build the FLAC section of the dialog. This will ask tag related questions
    # if the user wishes to utilise them.
    def __generate_flac_section(self):
        self.__layout_flac = QFormLayout()
        self.__lbl_flac = QLabel("FLAC Tags:")

        self.__le_title = QLineEdit()
        self.__le_title.setPlaceholderText("Title")
        self.__le_title.textChanged.connect(self.__on_title_change)

        self.__le_artist = QLineEdit()
        self.__le_artist.setPlaceholderText("Artist")
        self.__le_artist.textChanged.connect(self.__on_artist_change)

        self.__le_band = QLineEdit()
        self.__le_band.setPlaceholderText("Band")
        self.__le_band.textChanged.connect(self.__on_band_change)

        self.__le_album = QLineEdit()
        self.__le_album.setPlaceholderText("Album")
        self.__le_album.textChanged.connect(self.__on_album_change)

        layout_release_date = QHBoxLayout()
        self.__lbl_release_date = QLabel("Release Date: ")
        self.__de_release_date = QDateEdit()
        self.__de_release_date.dateChanged.connect(self.__on_release_date_change)
        layout_release_date.addWidget(self.__lbl_release_date)
        layout_release_date.addWidget(self.__de_release_date)

        self.__le_comment = QLineEdit()
        self.__le_comment.setPlaceholderText("Comment")
        self.__le_comment.textChanged.connect(self.__on_comment_change)

        self.__le_copyright = QLineEdit()
        self.__le_copyright.setPlaceholderText("Copyright")
        self.__le_copyright.textChanged.connect(self.__on_copyright_change)

        self.__layout_flac.addRow(self.__lbl_flac)
        self.__layout_flac.addRow(self.__le_title)
        self.__layout_flac.addRow(self.__le_artist)
        self.__layout_flac.addRow(self.__le_band)
        self.__layout_flac.addRow(self.__le_album)
        self.__layout_flac.addRow(layout_release_date)
        self.__layout_flac.addRow(self.__le_comment)
        self.__layout_flac.addRow(self.__le_copyright)


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

        self.__layout_root.addWidget(button_box)


# Helper methods

    def __remove_flac_section(self):
        # Clear all widgets from layout_flac
        while self.__layout_flac.count():
            item = self.__layout_flac.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            elif item.layout():
                self.__remove_flac_section_from_parent(item.layout())

        # Optionally, if you want to remove the layout_flac from the parent layout
        if self.__layout_root:
            self.__layout_root.removeItem(self.__layout_flac)

        # Destroy the layout if necessary
        self.__layout_flac.deleteLater()


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


    def __init_flac_tags(self):
        if self.__video.flac_tags is None: self.__video.flac_tags = FlacTags()