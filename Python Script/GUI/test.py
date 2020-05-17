
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        main_container = Container()
        main_container.attr_editor_newclass = False
        main_container.css_height = "345.0px"
        main_container.css_left = "20px"
        main_container.css_margin = "0px"
        main_container.css_position = "absolute"
        main_container.css_top = "20px"
        main_container.css_width = "330.0px"
        main_container.variable_name = "main_container"
        vbox0 = VBox()
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "center"
        vbox0.css_background_color = "rgb(0,0,0)"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "250px"
        vbox0.css_justify_content = "space-around"
        vbox0.css_left = "30.0px"
        vbox0.css_margin = "0px"
        vbox0.css_position = "absolute"
        vbox0.css_top = "75.0px"
        vbox0.css_width = "250px"
        vbox0.variable_name = "vbox0"
        voltageButton = Button()
        voltageButton.attr_editor_newclass = False
        voltageButton.css_height = "30px"
        voltageButton.css_margin = "0px"
        voltageButton.css_order = "139660924894352"
        voltageButton.css_position = "static"
        voltageButton.css_top = "20px"
        voltageButton.css_width = "100px"
        voltageButton.text = "Voltage"
        voltageButton.variable_name = "voltageButton"
        vbox0.append(voltageButton,'voltageButton')
        button1 = Button()
        button1.attr_editor_newclass = False
        button1.css_height = "30px"
        button1.css_margin = "0px"
        button1.css_order = "139660915754512"
        button1.css_position = "static"
        button1.css_top = "20px"
        button1.css_width = "100px"
        button1.text = "button"
        button1.variable_name = "button1"
        vbox0.append(button1,'button1')
        button2 = Button()
        button2.attr_editor_newclass = False
        button2.css_height = "30px"
        button2.css_margin = "0px"
        button2.css_order = "139660924598032"
        button2.css_position = "static"
        button2.css_top = "20px"
        button2.css_width = "100px"
        button2.text = "button"
        button2.variable_name = "button2"
        vbox0.append(button2,'button2')
        main_container.append(vbox0,'vbox0')
        

        self.main_container = main_container
        return self.main_container
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
