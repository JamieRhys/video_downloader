from enum import Enum

from entities.FlacTags import FlacTags


class VideoType(Enum):
    Single = 0,
    PlayList = 1,


class Video:
    def __init__(self,
                 output_dir: str = "",
                 url: str = "",
                 output_name: str = "",
                 video_type: VideoType = VideoType.Single,
                 convert: bool = True,
                 delete: bool = True,
                 flac_tags: FlacTags = None
    ):
        self.__output_dir = output_dir
        self.__url = url
        self.__output_name = output_name
        self.__video_type = video_type
        self.__convert = convert
        self.__delete = delete
        self.__flac_tags = flac_tags


    @property
    def output_dir(self): return self.__output_dir

    @property
    def url(self): return self.__url

    @url.setter
    def url(self, value: str): self.__url = value

    @property
    def output_name(self): return self.__output_name

    @output_name.setter
    def output_name(self, value: str): self.__output_name = value

    @property
    def video_type(self): return self.__video_type

    @video_type.setter
    def video_type(self, value: VideoType): self.__video_type = value

    @property
    def convert(self): return self.__convert

    @convert.setter
    def convert(self, state: bool): self.__convert = state

    @property
    def delete(self): return self.__delete

    @delete.setter
    def delete(self, state: bool): self.__delete = state

    @property
    def flac_tags(self): return self.__flac_tags

    @flac_tags.setter
    def flac_tags(self, value: FlacTags): self.__flac_tags = value


    def __str__(self):
        return "output_dir: " + self.__output_dir + "\n" + \
            "url: " + self.__url + "\n" + \
            "output_name: " + self.__output_name + "\n" + \
            "video_type: " + str(self.__video_type) + "\n" + \
            "convert: " + str(self.__convert) + "\n" + \
            "delete: " + str(self.__delete) + "\n" + \
            "flac_tags: " + "\n" + str(self.__flac_tags)