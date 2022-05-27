from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #create textures========================================================
        self.cloud_texture = Image(source = "cloud4.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width/self.cloud_texture.width,-1)
        self.floor_texture = Image(source = "floor2.jpg").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width/self.floor_texture.width,-1)
        self.sun_texture = Image(source = "sun.png").texture
        self.sun_texture.uvsize = (Window.width/self.sun_texture.width,-1)
        self.sound = SoundLoader.load('8bitmenu.wav')
        self.sound.play()

    def scroll_textures(self, time_passed):
        #Update the uvpos
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] - time_passed/20) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed/8) % Window.width, self.floor_texture.uvpos[1])
        #Redraw textures
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)

class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)

    def poop(self):
        self.dog_bark = SoundLoader.load('dog.wav')
        #print("Bark")
        self.dog_bark.play()
    pass


MainApp().run()
