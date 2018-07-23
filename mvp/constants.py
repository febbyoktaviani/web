class ErrorTemplateMessage():
    def __init__(self, param=None):
        self.param = param
    
    def not_found(self):
        return '%s not found' % self.param

    def missing_required(self):
        return '%s is missing and could not be empty'
