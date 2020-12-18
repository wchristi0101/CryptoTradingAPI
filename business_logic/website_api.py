import yaml
import master_functions
import pathlib


class Website:

    def __init__(self):
        self._config = "config.yml"
        self._website_settings = "website"
        self._website = None
        self._username = None
        self._password = None

    def _set_website(self, website_name: str):
        self._website = website_name

    def _set_username_password(self):
        configure = LoadYAML(self._config)
        if self._website is not None:
            username_password = configure.load_configuration((self._website_settings, self._website))
            self._username = username_password.get("username")
            self._password = username_password.get("password")

    def login(self) -> tuple:
        return self._username, self._password


class Bittrex(Website):
    def __init__(self):
        super().__init__()
        self._set_website("bittrex")
        self._set_username_password()


class LoadYAML:
    def __init__(self, yaml_document_name: str):
        self._yaml_document = master_functions.get_base_directory() / yaml_document_name

    def load_configuration(self, path_through_yaml: tuple):
        with open(self._yaml_document) as yaml_document:
            dictionary_output = yaml.load(yaml_document, Loader=yaml.FullLoader)
        for specified_items in path_through_yaml:
            dictionary_output = dictionary_output.get(specified_items)

        return dictionary_output
