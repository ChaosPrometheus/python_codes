
from kivy.app import App
from kivy.uix.video import Video
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top',  500)
Config.set('graphics', 'resizable', 'False')
#Config.set('graphics', 'borderless',  1)
Config.set('graphics', 'width', 1127)
Config.set('graphics', 'height', 636)

class MyApp(App):

    video = None
    def build(self):
        Window.bind(on_keyboard=self.on_keyboard)  # bind our handler
        self.video = Video(source='AC_DC - T.N.T.mp4', state='play', options={'aspect_ratio': True})
        self.video.state='play'
        #self.video.options = {'eos': 'loop'}
        self.video.allow_stretch=True
        self.video.pos_hint = {'top': 1.0}
        self.video.bind(eos=self.VideoDone)
        return self.video

    def VideoDone(self, value, value2):
        print ("video done", value, value2)

    def on_stop(self):
        print ('stopping and closing kivy')

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        print (window, key, scancode, codepoint, modifier)
        if codepoint == 'p':
            print ('pausing with p pressed')
            self.video.state='stop'
        if codepoint == 's':
            print ('starting with s pressed')
            self.video.state='play'
        if codepoint == 'r':
            print ('re-starting with r pressed')
            self.video.seek(0, precise=True)

if __name__ == '__main__':
    print ("hi")
    MyApp().run()