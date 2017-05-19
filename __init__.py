from adapt.intent import IntentBuilder;

from mycroft.util.log import getLogger;
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = "Tools UI"
LOG = getLogger(__name__)

class MagicMirrorSkill(MycroftSkill):
    def __init__(self):
        super(MagicMirrorSkill, self).__init__("MagicMirrorSkill")

    def initialize(self):
        intent = IntentBuilder("SoftwareAGIntent").require("SoftwareAGKeyword").build()
        self.register_intent(intent, self.softwareag_intent)

        intent = IntentBuilder("NameIntent").require("NameKeyword").build()
        self.register_intent(intent, self.name_intent)

    def name_intent(self, message):
        try:
            name = message.data.get("NameKeyword", None)
            self.speak_dialog(name)
        except:
            raise ValueError("Name not found")

    def softwareag_intent(self, message):
        self.speak_dialog("softwareag")

    def stop(self):
        pass

def create_skill():
    return MagicMirrorSkill()