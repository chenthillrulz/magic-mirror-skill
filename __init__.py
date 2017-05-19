from adapt.intent import IntentBuilder;

from mycroft.util.log import getLogger;
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import sys
sys.path.append('/opt/mycroft/skills/magic-mirror-skill')
from server_helper import RestHelper

__author__ = "Tools UI"
LOG = getLogger(__name__)

class MagicMirrorSkill(MycroftSkill):
    def __init__(self):
        super(MagicMirrorSkill, self).__init__("MagicMirrorSkill")
        self.rh = RestHelper()

    def initialize(self):
        intent = IntentBuilder("SoftwareAGIntent").require("SoftwareAGKeyword").build()
        self.register_intent(intent, self.softwareag_intent)

        intent = IntentBuilder("NameIntent").require("NameKeyword").build()
        self.register_intent(intent, self.name_intent)

        intent = IntentBuilder("TrafficIntent").require("TrafficKeyword").require("LocationsKeyword").build()
        self.register_intent(intent, self.traffic_intent)

        intent = IntentBuilder("DirectionIntent").require("DirectionsKeyword").require("LocationsKeyword").build()
        self.register_intent(intent, self.direction_intent)

    def name_intent(self, message):
        try:
            name = message.data.get("NameKeyword", None)
            self.speak_dialog(name)
        except:
            raise ValueError("Name not found")

    def traffic_intent (self, message):
        try:
            location = message.data.get("LocationsKeyword", None)
            self.rh.get_traffic(location)
        except:
            raise ValueError("Location Not Found")

    def direction_intent (self, message):
        try:
            location = message.data.get("LocationsKeyword", None)
            self.rh.get_direction(location)
        except Exception,e:
            print (str(e))
            raise ValueError("Location Not found")


    def softwareag_intent(self, message):
        self.speak_dialog("softwareag")

    def stop(self):
        pass

def create_skill():
    return MagicMirrorSkill()
