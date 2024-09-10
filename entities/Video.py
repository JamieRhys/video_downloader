from entities.FlacTags import FlacTags


class Video:
    def __init__(self,
                 output_dir: str = "",
                 url: str = "",
                 output_name: str = "",
                 convert: bool = True,
                 delete: bool = True,
                 flac_tags: FlacTags = None
    ):
        self.__output_dir = output_dir
        self.__url = url
        self.__output_name = output_name
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
    def convert(self): return self.__convert

    @convert.setter
    def convert(self, state: bool): self.__convert = state

    @property
    def delete(self): return self.__delete

    @property
    def flac_tags(self): return self.__flac_tags