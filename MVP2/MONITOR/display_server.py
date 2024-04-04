class DisplayServer():

    def __init__(self, getway):
        self.getway = getway

    def display(self, lines):
        result = self.getway.service_call(
            service_name="DisplayServer",
            endpoint="/display",
            data={"lines": lines}
        )

        return result
