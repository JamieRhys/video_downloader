# VD - Video Downloader
#### Video Demo:  <URL HERE>
#### Description:
Video Downloader (VD for short) is a program complete with a Graphical User Interface that downloads
one or more videos from YouTube and then convert it into a FLAC audio file. Finally, it will then
delete the downloaded video at the user's request.

## Design

### The GUI
For the Graphical User Interface, I have a number of options to choose from:

1. CLI - Command Line Interface
   - The easiest to implement. The CLI is also the most time-consuming for the user as they will need to
   write each and every argument out in a specific order. 
2. [Tkinter](https://docs.python.org/3/library/tkinter.html)
    - Used to create simple GUI's and small applications. This library is also the defacto for Python.
   It's the only framework built into Python and is also cross-platform, available on Windows, macOS and
   Linux. This is the easiest to implement on the GUI front, however it has no support for being driven
   by data sources or databases and is not suitable for manipulating multimedia or hardware.
3. [PyQt](https://wiki.python.org/moin/PyQt)
    - Not as easy to implement as Tkinter, however it's the easiest way to create modern interfaces 
   and is a wrapper around the Qt framework, a long-standing C++ GUI framework. This is a complete
   development library and not just a framework. It provides standard UI components such as widgets and
   layouts. It also provides MVC-like data-driven views (spreadsheets, tables) database interfaces, modes
   and so on. This is perfect to create applications for multimedia.
4. [PySimpleGUI](https://www.pysimplegui.com/pricing) 
    - Unfortunately, upon looking into this framework, I found that this relies on a paid-for licence
   model. This is, by default, ruled out due to this.
5. [WxPython](https://wxpython.org/index.html)
   - WxPython is a wrapper around the popular GUI Toolkit WxWidgets. It's cross-platform and available
   for Windows, macOS and Linux. WxPython is under active development and has been reimplemented from 
   scratch. It does not provide the level of abstraction that Qt does. 

#### Decision:
Although a CLI interface would be the easiest to implement, I want it to be easy to use for the average
user. I also want to be able to give the user the ability to choose from one or more videos to download
which requires the use of a list of URL's that can be added to or removed from. Because of this, I have
decided to use PyQt due to it implementing data source driven and database driven support. Of course,
PyQt is going to be harder to implement but the reward outweighs the risk.

