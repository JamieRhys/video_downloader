from typing import List

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSpacerItem, \
    QSizePolicy, QListWidget, QFileDialog

from dialogs.AddVideoDialog import AddVideoDialog
from entities.Video import Video


# Subclass QMainWindow to customise the application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Video Downloader")

        self.__videos: List[Video] = []

        self.__init_ui_components()
        self.__setup_layouts()





### Component Initialisation Functions


    """ 
        Initialises all UI Components used in the main window. They are then available
        throughout the MainWindow class 
    """
    def __init_ui_components(self):
    # Top Layout Components
        self.__le_output_dir = QLineEdit()
        self.__le_output_dir.setPlaceholderText("Output Directory")

        self.__btn_browse = QPushButton("Browse")
        self.__btn_browse.clicked.connect(self.__on_browse_button_clicked)

    # Middle Layout Components
        self.__lw_videos = QListWidget()
        self.__lw_videos.itemSelectionChanged.connect(self.__on_video_selected)

    # Bottom Layout Components
        self.__btn_download = QPushButton("Download")
        self.__btn_download.clicked.connect(self.__on_download_button_clicked)
        self.__btn_add = QPushButton("Add")
        self.__btn_add.clicked.connect(self.__on_add_button_clicked)
        self.__btn_remove = QPushButton("Remove")
        self.__btn_remove.clicked.connect(self.__on_remove_button_clicked)




### Layout Creation Methods


    """ Sets up the layout of the main window. """
    def __setup_layouts(self):
        widget_root = QWidget()
        layout_root = QVBoxLayout()

        layout_root.addLayout(self.__create_top_layout())
        layout_root.addLayout(self.__create_middle_layout())
        layout_root.addLayout(self.__create_bottom_layout())

        widget_root.setLayout(layout_root)
        self.setCentralWidget(widget_root)



    def __create_top_layout(self):
        layout = QHBoxLayout()

        layout.addWidget(self.__le_output_dir)
        layout.addWidget(self.__btn_browse)

        return layout


    def __create_middle_layout(self):
        layout = QVBoxLayout()
        layout.setStretch(0, 1)

        layout.addWidget(self.__lw_videos)

        return layout


    def __create_bottom_layout(self):
        layout = QHBoxLayout()
        layout_buttons = QHBoxLayout()

        layout_buttons.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        layout_buttons.addWidget(self.__btn_add)
        layout_buttons.addWidget(self.__btn_remove)
        layout.addWidget(self.__btn_download)
        layout.addLayout(layout_buttons)

        return layout



    """ Called when we need to add a new video to our list """
    def __add_video(self, video: Video):
        pass




### On Change Handler Methods


    def __on_video_selected(self):
        pass




### On Click Handler Methods


    """ Called when the browse button is clicked. """
    def __on_browse_button_clicked(self):
        # Open a file dialog so the user can select an output directory.
        dir_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")

        if dir_path:
            # if the directory exists, set the text of our line edit so the user can see/edit it.
            self.__le_output_dir.setText(dir_path)

            # Iterate through each video (if any exist in the list)
            for video in self.__videos:
                # Update the output dir variable to correctly align with where it should be stored.
                video.output_dir = dir_path


    def __on_download_button_clicked(self):
        pass


    """ 
        When the user wants to add a new video, this will be called which will open a dialog 
        window to ask the relevant questions.
    """
    def __on_add_button_clicked(self):
        dlg = AddVideoDialog()
        # dlg.avd_signal_new_video(self.__add_video)
        dlg.exec()


    def __on_remove_button_clicked(self):
        pass