# MikroKamK
Kivy version of MikroKam, which used Tkinter

Although the original MikroKam works well, I found the Tkinter tools quite frustrating and it was very difficult to get the presentation on the Raspberry Pi Touchscreen to work the way I envisioned it.

Rather than fighting it, I decided to further my education in graphics programming by tackling a new version using Kivy.

The learning curve was not too steep, since my background with Windows programming and Delphi/Lazarus gave me a good understanding of how GUI programs work. It only took part of a day to get the basic skeleton working and the screen presentation is very close to what I want. These are the features that are in the plan:

* Sliders to control brightness and contrast on the main screen. (Done)
* The preview button, when pressed, will start the preview and change the button to STOP the preview. It will also disable any controls that should not be activated during a preview. The Pi camera preview mode can leave the screen unusable if the preview is not gracefully stopped.
* A file status at the top of the image window to show if the USB is missing, and the last file that was saved.
* a MENU button to take the user to one or more screens for managing the Kivy config file and the saved snapshots. This may involve several screens.
* A more thorough emulation of the Pi environment on a Linux desktop. Development on that tiny screen is impossible. We can detect the environment and "pretend" to have a camera attached for testing. It isn't hard to port the program over to the Pi through SSH, but you really need a good working environment for development.

There have been a few interesting challenges. The vanilla Raspbian distribution makes the installation of Kivy a long and painful process and I was never able to get the Kivy examples working right. Then I found kivypie which is a complete Kivy distribution that just works.
So as of now ( 22 Feb 2018 ) I have posted the first code which is really just the mockup of the main screeen.
