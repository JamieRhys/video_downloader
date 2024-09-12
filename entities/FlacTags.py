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
                 tracks: str = None,
                 disc_num: str = None,
                 disc_nums: str = None,
                 composers: str = None,
                 track_copyright: str = None,
                 genres: Genres = None,
    ):
        self.__title = title
        self.__artist = artist
        self.__band = band
        self.__album = album
        self.__release_date = release_date
        self.__comment = comment
        self.__track = track
        self.__tracks = tracks
        self.__disc_num = disc_num
        self.__disc_nums = disc_nums
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

    @track.setter
    def track(self, value: str): self.__track = value

    @property
    def tracks(self): return self.__tracks

    @tracks.setter
    def tracks(self, value: str): self.__tracks = value

    @property
    def disc_num(self): return self.__disc_num

    @disc_num.setter
    def disc_num(self, value: str): self.__disc_num = value

    @property
    def disc_nums(self): return self.__disc_nums

    @disc_nums.setter
    def disc_nums(self, value: str): self.__disc_nums = value

    @property
    def composers(self): return self.__composers

    @composers.setter
    def composers(self, value: str): self.__composers = value

    @property
    def copyright(self): return self.__copyright

    @copyright.setter
    def copyright(self, value: str): self.__copyright = value

    @property
    def genres(self): return self.__genres

    @genres.setter
    def genres(self, value: Genres): self.__genres = value

    def __str__(self):
        return "\ttitle: " + str(self.__title) + "\n" + \
            "\tartist: " + str(self.__artist) + "\n" + \
            "\tband: " + str(self.__band) + "\n" + \
            "\talbum: " + str(self.__album) + "\n" + \
            "\trelease_date: " + str(self.__release_date) + "\n" + \
            "\tcomment: " + str(self.__comment) + "\n" + \
            "\ttrack: " + str(self.__track) + "/" + str(self.__tracks) + "\n" + \
            "\tdisc_num: " + str(self.__disc_num) + "\n" + \
            "\tcomposers: " + "None" if self.__composers is None else self.__composers + "\n" + \
            "\tcopyright: " + str(self.__copyright) + "\n" + \
            "\tgenres: " + "None" if self.__genres is None else ', '.join(genre for genre in self.__genres) + "\n"