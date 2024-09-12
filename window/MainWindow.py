from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QListWidget, \
    QSizePolicy, QFileDialog, QDialog

from dialogs.AddVideoDialog import AddVideoDialog
from entities.Video import Video
from utils.color import Color

# Subclass QMainWindow to customise the application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Video Downloader")
        self.__videos = []
        self.__list_videos = self.generate_list_videos()

        # Component Widgets
        self.btn_browse = QPushButton("Browse")
        self.btn_browse.clicked.connect(self.onBrowseButtonClicked)
        self.btn_add = QPushButton("Add")
        self.btn_add.clicked.connect(self.onAddButtonClicked)
        self.btn_remove = QPushButton("Remove")

        self.colorRed = Color("red")
        self.colorGreen = Color("green")
        self.colorBlue = Color("blue")

        self.le_output_dir = QLineEdit()
        self.le_output_dir.setPlaceholderText("Output Directory")

        # Layouts
        self.layout_list_buttons = self.generate_layout_list_buttons()
        self.layout_left = self.generate_layout_left()
        self.layout_right = self.generate_layout_right()
        self.layout_top = self.generate_layout_top()
        self.layout_bottom = self.generate_layout_bottom()
        self.layout_root = self.generate_layout_root()

        widget_root = QWidget()
        widget_root.setLayout(self.layout_root)
        self.setCentralWidget(widget_root)


# On Click Methods
    def onAddButtonClicked(self):
        dlg = AddVideoDialog()
        dlg.new_video.connect(self.add_video)
        dlg.exec()


    def __on_remove_button_clicked(self):


    def onBrowseButtonClicked(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")

        if directory_path:
            self.le_output_dir.setText(directory_path)


# Generate Layouts
    def generate_layout_list_buttons(self):
        layout_list_buttons = QHBoxLayout()
        layout_list_buttons.addWidget(self.btn_add)
        layout_list_buttons.addWidget(self.btn_remove)

        return layout_list_buttons

    def generate_layout_left(self):
        layout_left = QVBoxLayout()
        layout_left.addWidget(self.__list_videos)
        layout_left.addLayout(self.layout_list_buttons)

        return layout_left


    def generate_layout_right(self):
        layout_right = QVBoxLayout()
        layout_right.addWidget(self.colorBlue)

        return layout_right


    def generate_layout_top(self):
        layout_top = QHBoxLayout()
        layout_top.addWidget(self.le_output_dir)
        layout_top.addWidget(self.btn_browse)

        return layout_top


    def generate_layout_bottom(self):
        layout_bottom = QHBoxLayout()
        layout_bottom.addLayout(self.layout_left)
        layout_bottom.addLayout(self.layout_right)
        layout_bottom.setStretch(0, 0)
        layout_bottom.setStretch(1, 1)

        return layout_bottom


    def generate_layout_root(self):
        layout_root = QVBoxLayout()
        layout_root.addLayout(self.layout_top)
        layout_root.addLayout(self.layout_bottom)

        return layout_root


# Generate Widgets
    def generate_list_videos(self):
        list_videos = QListWidget()
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

    def add_video(self, video: Video):
        self.__videos.append(video)
        self.__refresh_video_list()