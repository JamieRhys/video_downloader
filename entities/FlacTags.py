from typing import List

from entities.Genres import Genres


# ID3 v2.4 Tags that are relevant to us here are as follows:
# +--------+-----------------------+----------+---------------------------------------+
# | Tag ID | Tag Name              | Writable | Values/Notes                          |
# +--------+-----------------------+----------+---------------------------------------+
# | 'COMM' | Comment               | No       |                                       | /
# | 'TALB' | Album                 | No       |                                       | /
# | 'TCON' | Genre                 | No       | Uses same lookup table as ID3v1 Genre | /
# | 'TCOP' | Copyright             | No       |                                       | /
# | 'TDRL' | Release Time          | No       | Stored as YYYY-MM-DD                  | /
# | 'TIT2' | Title                 | No       |                                       | /
# | 'TPE1' | Artist                | No       |                                       | /
# | 'TPE2' | Band                  | No       |                                       | /
# | 'TRCK' | Track                 | No       | Can be stored as 1/10                 | /
# | 'TPOS' | Disc number           | No       | Can be stored as 1/1                  | /
# | 'TCOM' | Composer              | No       |                                       | /
# +--------+-----------------------+----------+---------------------------------------+

class FlacTags:
    def __init__(self,
                 title: str = None,
                 artist: str = None,
                 band: str = None,
                 album: str = None,
                 release_date: str = None,
                 comment: str = None,
                 track: str = None,
                 disc_num: str = None,
                 composers: List[str] = None,
                 track_copyright: str = None,
                 genres: List['Genres'] = None,
    ):
        self.__title = title
        self.__artist = artist
        self.__band = band
        self.__album = album
        self.__release_date = release_date
        self.__comment = comment
        self.__track = track
        self.__disc_num = disc_num
        self.__composers = composers
        self.__copyright = track_copyright
        self.__genres = genres

    @property
    def title(self): return self.__title

    @title.setter
    def title(self, value: str): self.__title = value

    @property
    def artist(self): return self.__artist

    @artist.setter
    def artist(self, value: str): self.__artist = value

    @property
    def band(self): return self.__band

    @band.setter
    def band(self, value: str): self.__band = value

    @property
    def album(self): return self.__album

    @album.setter
    def album(self, value: str): self.__album = value

    @property
    def release_date(self): return self.__release_date

    @release_date.setter
    def release_date(self, value: str): self.__release_date = value

    @property
    def comment(self): return self.__comment

    @comment.setter
    def comment(self, value: str): self.__comment = value

    @property
    def track(self): return self.__track

    @property
    def disc_num(self): return self.__disc_num

    @property
    def composers(self): return self.__composers

    @property
    def copyright(self): return self.__copyright

    @copyright.setter
    def copyright(self, value: str): self.__copyright = value

    @property
    def genres(self): return self.__genres

    def __str__(self):
        return "\ttitle: " + str(self.__title) + "\n" + \
            "\tartist: " + str(self.__artist) + "\n" + \
            "\tband: " + str(self.__band) + "\n" + \
            "\talbum: " + str(self.__album) + "\n" + \
            "\trelease_date: " + str(self.__release_date) + "\n" + \
            "\tcomment: " + str(self.__comment) + "\n" + \
            "\ttrack: " + "\n" + \
            "\tdisc_num: " + "\n" + \
            "\tcomposers: " + "\n" + \
            "\tcopyright: " + str(self.__copyright) + "\n" + \
            "\tgenres: " + "\n"