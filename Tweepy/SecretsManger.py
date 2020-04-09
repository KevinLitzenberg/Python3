from configparser import ConfigParser
import logging

# version 0.0.1
class configManager:
   
    def __init__(self, config_file):
        
        self.config_sections = []

        self.secrets_filename = config_file

        # instantiate
        self.config = ConfigParser()

        # parse existing file
        self.config.read(config_file)

    def get_config_value(self,section, key):
        return self.config.get(section, key)

    def print_config_key(self,section, key):
        print(self.config.get(section,key))

    def set_config_key(self,section, key, value):
        self.config.set(section,key,value)

    def save_config_file(self):
        with open(self.secrets_filename, "w") as configfile:
            self.config.write(configfile)

    # section functions
    def add_section(self,section):
        self.config.add_section(section)

    def get_sections(self):
        #global config_sections
        self.config_sections = self.config.sections()

    def print_sections(self):
        #global config_sections
        print(f"section:")

        for i in self.config_sections:
           print(f"  {i}")

