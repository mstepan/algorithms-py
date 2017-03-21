

class OldResistor(object):

    def __init__(self, ohms):
        self._ohms = ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError("'ohms' field can't be negative: %s" % ohms)

        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute _ohms")

        self._ohms = ohms


    def __str__(self):
        return "%s OM" % self._ohms


