from mycroft import MycroftSkill, intent_file_handler


class Generateuuid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('generateuuid.intent')
    def handle_generateuuid(self, message):
        self.speak_dialog('generateuuid')


def create_skill():
    return Generateuuid()

