# debouncer.py

class Debouncer:
    def __init__(self, pin, debounce_time=50):
        """
        Initialize the debouncer.

        :param pin: The pin to debounce.
        :param debounce_time: The debounce time in milliseconds.
        """
        self.pin = pin
        self.debounce_time = debounce_time
        self.last_state = None
        self.last_change = 0

    def read(self):
        """
        Read the debounced state of the pin.

        :return: The debounced state of the pin.
        """
        from time import ticks_ms
        current_state = self.pin.value()
        current_time = ticks_ms()

        if current_state != self.last_state:
            if current_time - self.last_change < self.debounce_time:
                return self.last_state
            else:
                self.last_state = current_state
                self.last_change = current_time

        return current_state

    def __call__(self):
        """
        Alias for read().
        """
        return self.read()
