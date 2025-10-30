from utilities import GlobalVars

class HeaderUtils:
    def __init__(self):
        self.user_agent_header = GlobalVars.user_agent_header
        self.location_header = GlobalVars.location_header

    
    def get_user_agent(self):
        return self.user_agent_header

    def get_location(self):
        return self.location_header