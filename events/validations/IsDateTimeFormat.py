import datetime
from events.validations.RuleAbstract import RuleAbstract


class IsDateTimeFormat(RuleAbstract):

    def handle_request(self):
        try:
            datetime.datetime.strptime(self.event[self.field], self.value)
            return self._successor.handle_request() if self._successor is not None else True
        except ValueError:
            return False
