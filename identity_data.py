class IdentityData:
    def __init__(self, identity, details):
        self.identity = identity
        self.details = details

    def to_dict(self):
        return {
            'identity': self.identity,
            'details': self.details
        }

