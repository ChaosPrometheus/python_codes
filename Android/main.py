from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(App):
    def build(self):
        btn_layout = GridLayout(cols=2)
        left_layout = AnchorLayout(anchor_x='left', anchor_y='bottom')
        left_layout.add_widget(Button(text='Левый', width=60, height=40, size_hint_x=0.50, size_hint_y=0.50))
        right_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        right_layout.add_widget(Button(text='Правый', width=60, height=40, size_hint_x=0.50, size_hint_y=0.50))
        
        btn_layout.add_widget(left_layout)
        btn_layout.add_widget(right_layout)

        full_layout = GridLayout(rows=2)
        full_layout.add_widget(Label(text="Приложение"))
        full_layout.add_widget(btn_layout)

        return full_layout

if __name__ == '__main__':
    MyApp().run()