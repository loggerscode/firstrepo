#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk

#win = Gtk.Window()
#win.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Mein erstes Programm")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hallo Welt!")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
