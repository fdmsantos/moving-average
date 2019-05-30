import datetime
from RuleAbstract import RuleAbstract


class IsDateTimeFormat(RuleAbstract):

    def handle_request(self):
        try:
            datetime.datetime.strptime(self.event[self.field], self.value)
            return True
        except ValueError:
            return False
