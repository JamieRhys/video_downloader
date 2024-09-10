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
                 title: str,
                 artist: str,
                 band: str,
                 album: str,
                 release_time: str,
                 comment: str,
                 track: str,
                 disc_num: str,
                 composers: List[str],
                 track_copyright: str,
                 genres: List['Genres']
                 ):
        self.__title = title
        self.__artist = artist
        self.__band = band
        self.__album = album
        self.__release_time = release_time
        self.__comment = comment
        self.__track = track
        self.__disc_num = disc_num
        self.__composers = composers
        self.__copyright = track_copyright
        self.__genres = genres

    @property
    def title(self): return self.__title

    @property
    def artist(self): return self.__artist

    @property
    def band(self): return self.__band

    @property
    def album(self): return self.__album

    @property
    def release_time(self): return self.__release_time

    @property
    def comment(self): return self.__comment

    @property
    def track(self): return self.__track

    @property
    def disc_num(self): return self.__disc_num

    @property
    def composers(self): return self.__composers

    @property
    def copyright(self): return self.__copyright

    @property
    def genres(self): return self.__genres