from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QListWidget, \
    QSizePolicy, QFileDialog, QMessageBox, QLabel, QTextEdit, QStackedWidget
from debian.debtags import output

from dialogs.AddVideoDialog2 import AddVideoDialog
from entities.Video import Video
from utils.color import Color

# Subclass QMainWindow to customise the application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Video Downloader")
        self.__selected_video = None
        self.__videos = []
        self.__list_videos = self.__generate_list_videos()

        # Component Widgets
        self.__btn_browse = QPushButton("Browse")
        self.__btn_browse.clicked.connect(self.__on_browse_button_clicked)
        self.__btn_add = QPushButton("Add")
        self.__btn_add.clicked.connect(self.__on_add_button_clicked)
        self.__btn_remove = QPushButton("Remove")
        self.__btn_remove.clicked.connect(self.__on_remove_button_clicked)

        self.colorRed = Color("red")
        self.colorGreen = Color("green")
        self.colorBlue = Color("blue")

        self.__le_output_dir = QLineEdit()
        self.__le_output_dir.setPlaceholderText("Output Directory")
        self.__le_output_dir.textChanged.connect(self.__on_output_dir_change)

        self.__stacked_widget = QStackedWidget()

        self.__video_info_panel = self.__generate_video_info_panel()
        self.__conversion_info_panel = self.__generate_conversion_info_panel()
        self.__stacked_widget.addWidget(self.__video_info_panel)
        self.__stacked_widget.addWidget(self.__conversion_info_panel)

        # Layouts
        self.__layout_list_buttons = self.__generate_layout_list_buttons()
        self.__layout_left = self.__generate_layout_left()
        self.__layout_right = self.__generate_layout_right()
        self.__layout_top = self.__generate_layout_top()
        self.__layout_bottom = self.__generate_layout_bottom()
        self.__layout_root = self.__generate_layout_root()

        widget_root = QWidget()
        widget_root.setLayout(self.__layout_root)
        self.setCentralWidget(widget_root)


# On Click Methods
    def __on_add_button_clicked(self):
        dlg = AddVideoDialog()
        dlg.new_video.connect(self.__add_video)
        dlg.exec()


    def __on_remove_button_clicked(self):
        # Let's first find the selected video.
        selected_videos = self.__list_videos.selectedItems()

        if not selected_videos:
            return  # nothing is currently selected.

        # Confirmation dialog just to be sure the user actually wants to delete the video.
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Just to be sure!")
        dlg.setText("Are you sure you want to delete this video?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            # If the user is sure and taps yes, search for the item in the selected videos (if more than one is selected).
            for item in selected_videos:
                # Get the video name.
                video_name = item.text()
                # if the name matches what we have in videos (output name or url), add it to be removed.
                video_to_remove = next((v for v in self.__videos if v.output_name == video_name or v.url == video_name))

                # Final check to make sure that the video is not None or anything.
                if video_to_remove:
                    # Remove the video from videos
                    self.__videos.remove(video_to_remove)
                    # Remove the entry from the list of videos too (this is actually displayed to the user).
                    self.__list_videos.takeItem(self.__list_videos.row(item))


    def __on_browse_button_clicked(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")

        if directory_path:
            self.__le_output_dir.setText(directory_path)


# On Change Methods

    def __on_output_dir_change(self, value: str):
        for video in self.__videos:
            video.output_dir = value


# Other On Methods

    def __on_video_selected(self):
        item = self.__list_videos.currentItem().text()

        for video in self.__videos:
            if item == video.output_name or item == video.url:
                self.__selected_video = video

        # Show the video info panel
        self.__update_video_info_panel()
        self.__stacked_widget.setCurrentWidget(self.__video_info_panel)


# Generate Layouts

    def __generate_video_info_panel(self):
        panel = QWidget()
        layout = QVBoxLayout()
        self.__lbl_video_info = QLabel("Video Information")

        # URL
        url_container = QHBoxLayout()
        self.__lbl_url = QLabel("URL: ")
        self.__le_url = QLineEdit()
        self.__le_url.setText("None" if self.__selected_video is None else self.__selected_video.url)
        self.__le_url.setEnabled(False)
        url_container.addWidget(self.__lbl_url)
        url_container.addWidget(self.__le_url)

        # Output Name
        output_name_container = QHBoxLayout()
        self.__lbl_output_name = QLabel("Output Name: ")
        self.__le_output_name = QLineEdit()
        self.__le_output_name.setText("None" if self.__selected_video is None else self.__selected_video.output_name)
        output_name_container.addWidget(self.__lbl_output_name)
        output_name_container.addWidget(self.__le_output_name)

        # TODO: Continue adding the remainder of fields here.

        layout.addWidget(self.__lbl_video_info)
        layout.addLayout(url_container)
        layout.addLayout(output_name_container)
        panel.setLayout(layout)
        return panel

    def __update_video_info_panel(self):
        if self.__selected_video is not None:
            self.__le_url.setText(self.__selected_video.url)
            self.__le_output_name.setText(self.__selected_video.output_name)
            # TODO: Continue adding remaining fields to update here.
            # TODO: Refactor code


    def __generate_conversion_info_panel(self):
        panel = QWidget()
        layout = QVBoxLayout()
        self.__output_text = QTextEdit()
        self.__output_text.setReadOnly(True)
        layout.addWidget(self.__output_text)
        panel.setLayout(layout)

        return panel


    def __generate_layout_list_buttons(self):
        layout_list_buttons = QHBoxLayout()
        layout_list_buttons.addWidget(self.__btn_add)
        layout_list_buttons.addWidget(self.__btn_remove)

        return layout_list_buttons

    def __generate_layout_left(self):
        layout_left = QVBoxLayout()
        layout_left.addWidget(self.__list_videos)
        layout_left.addLayout(self.__layout_list_buttons)

        return layout_left


    def __generate_layout_right(self):
        layout_right = QVBoxLayout()
        layout_right.addWidget(self.__stacked_widget)

        return layout_right


    def __generate_layout_top(self):
        layout_top = QHBoxLayout()
        layout_top.addWidget(self.__le_output_dir)
        layout_top.addWidget(self.__btn_browse)

        return layout_top


    def __generate_layout_bottom(self):
        layout_bottom = QHBoxLayout()
        layout_bottom.addLayout(self.__layout_left)
        layout_bottom.addLayout(self.__layout_right)
        layout_bottom.setStretch(0, 0)
        layout_bottom.setStretch(1, 1)

        return layout_bottom


    def __generate_layout_root(self):
        layout_root = QVBoxLayout()
        layout_root.addLayout(self.__layout_top)
        layout_root.addLayout(self.__layout_bottom)

        return layout_root


# Generate Widgets
    def __generate_list_videos(self):
        list_videos = QListWidget()
        list_videos.itemSelectionChanged.connect(self.__on_video_selected)
        for video in self.__videos:
            name = video.url if video.output_name is None else video.output_name
            list_videos.addItem(name)
        list_videos.setFixedWidth(400)
        list_videos.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        return list_videos


    def __refresh_video_list(self):
        self.__list_videos.clear()
        for video in self.__videos:
            name = video.output_name if video.output_name else video.url
            self.__list_videos.addItem(name)

    def __add_video(self, video: Video):
        video.output_dir = self.__le_output_dir.text()
        self.__videos.append(video)
        self.__refresh_video_list()