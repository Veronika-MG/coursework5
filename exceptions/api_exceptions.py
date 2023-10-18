class HHApiError(Exception):
    """
    Ошибка, вызываемая ошибкой от api.hh
    """
    def __init__(self, message):
        super().__init__(message)