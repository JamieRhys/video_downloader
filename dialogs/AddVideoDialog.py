# Re-write this class
from typing import List

from PyQt6.QtCore import pyqtSignal, QSize, Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget

from entities.FlacTags import FlacTags
from entities.Video import Video, VideoType
from utils import ComponentHelper


class AddVideoDialog(QDialog):
    avd_signal_new_video = pyqtSignal(Video)


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add new video")
        self.setMinimumWidth(800)

        self.__video = Video()

        self.__init_ui_components()
        self.__setup_layouts()




### Init Methods

    def __init_flac_tags(self):
        if self.__video.flac_tags is None:
            self.__video.flac_tags = FlacTags()




### Layout Creation Methods

    def __init_ui_components(self):
    # Button section components
        self.__btn_add_video = ComponentHelper.create_button("Add Video", self.__on_add_video_button_clicked)

    # Video Information Section Components
        self.__lbl_video_info = ComponentHelper.create_label("Video Information:")
        self.__lbl_video_type = ComponentHelper.create_label("Type ")

        self.__cmb_video_type = ComponentHelper.create_combo_box(placeholder="Type",
                                                                 items=[str(VideoType.SingleVideo), str(VideoType.PlayList)],
                                                                 current_item_index=int(self.__video.video_type),
                                                                 current_index_changed=self.__on_video_type_option_changed)
        self.__le_url = ComponentHelper.create_line_edit("URL", self.__on_url_text_changed)
        self.__le_output_name = ComponentHelper.create_line_edit("Output Name", self.__on_output_name_text_changed)

        self.__cb_convert = ComponentHelper.create_check_box("Convert to FLAC?", self.__video.convert, self.__on_convert_toggled)
        self.__cb_delete = ComponentHelper.create_check_box(text="Delete Original Video?",
                                                            is_checked=self.__video.delete,
                                                            is_enabled=self.__video.convert, # Linked to convert. If convert is not checked, we don't want the original video to be deleted.
                                                            tooltip="Only available when converting to FLAC.",
                                                            state_changed=self.__on_delete_toggled)

    # FLAC Tags section components
        self.__lbl_flac_tags = ComponentHelper.create_label("FLAC Tags:")


    def __setup_layouts(self):
        layout_root = QVBoxLayout()

        self.__widget_flac = QWidget()
        self.__widget_flac.setLayout(self.__create_layout_flac())
        if not self.__video.convert:
            self.__widget_flac.hide()

        layout_root.addLayout(self.__create_layout_video())
        layout_root.addWidget(self.__widget_flac)
        layout_root.addLayout(self.__create_layout_button())

        self.setLayout(layout_root)


    def __create_layout_video(self):
        layout = QVBoxLayout()

        container_video_type = QHBoxLayout()
        container_video_type.addItem(ComponentHelper.create_spacer_item())
        container_video_type.addWidget(self.__lbl_video_type)
        container_video_type.addWidget(self.__cmb_video_type)
        container_video_type.addItem(ComponentHelper.create_spacer_item())

        container_url_and_output_name = QHBoxLayout()
        container_url_and_output_name.addWidget(self.__le_url)
        container_url_and_output_name.addWidget(self.__le_output_name)

        container_convert_delete = QHBoxLayout()
        container_convert_delete.addItem(ComponentHelper.create_spacer_item())
        container_convert_delete.addWidget(self.__cb_convert)
        container_convert_delete.addItem(ComponentHelper.create_spacer_item())
        container_convert_delete.addWidget(self.__cb_delete)
        container_convert_delete.addItem(ComponentHelper.create_spacer_item())

        layout.addWidget(self.__lbl_video_info)
        layout.addLayout(container_video_type)
        layout.addLayout(container_url_and_output_name)
        layout.addLayout(container_convert_delete)

        return layout


    def __create_layout_flac(self):
        layout = QVBoxLayout()

        layout.addWidget(self.__lbl_flac_tags)

        return layout


    """ Creates the button layout which holds our Add button in the bottom center of the dialog"""
    def __create_layout_button(self):
        layout = QHBoxLayout()

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        layout.addWidget(self.__btn_add_video)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))

        return layout





### On Changed Handlers

    def __on_url_text_changed(self, text: str): self.__video.url = text


    def __on_output_name_text_changed(self, text: str): self.__video.output_name = text


    def __on_title_text_changed(self, text: str):
        self.__init_flac_tags()
        self.__video.flac_tags.title = text


    def __on_artist_text_changed(self, text: str):
        # TODO: Continue adding these fields.
        pass


    def __on_video_type_option_changed(self, value: int):
        match value:
            case VideoType.SingleVideo:
                self.__video.video_type = VideoType.SingleVideo
            case VideoType.PlayList:
                self.__video.video_type = VideoType.PlayList
            case _:
                self.__video.video_type = VideoType.SingleVideo




### On Click Handlers

    def __on_add_video_button_clicked(self):
        print("DONE")





### On Toggled Handlers

    def __on_convert_toggled(self, state):
        # Check if the state is checked.
        if state == Qt.CheckState.Checked.value:
            # If it is, reassign the video convert to true
            self.__video.convert = True
            # Enable delete original video as the user may want to delete it after converting.
            self.__cb_delete.setEnabled(True)
            # Show the FLAC Tags section to allow the user to fill out the relevant tags.
            self.__widget_flac.show()
        elif state == Qt.CheckState.Unchecked.value:
            # If it's unchecked, reassign convert to false
            self.__video.convert = False
            # Disable delete original video as we are not converting to FLAC, we don't need to
            # delete the video.
            self.__cb_delete.setEnabled(False)
            # Hide the FLAC Tags section as this is not needed.
            self.__widget_flac.hide()
            # Readjust the size of the window to remove the new space created.
            self.adjustSize()


    def __on_delete_toggled(self, state):
        if state == Qt.CheckState.Checked.value:
            self.__video.delete = True
        elif state == Qt.CheckState.Unchecked.value:
            self.__video.delete = False