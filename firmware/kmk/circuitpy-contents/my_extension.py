# Extension class to query VL53L0 ToF distance sensor 
# and do stuff based on values.

from kmk.extensions import Extension
# Import stuff here


class MyExtension(Extension):
    def after_hid_send(self, keyboard):
        # TODO: hook into event loop here
        return
        
    def on_runtime_enable(self, keyboard):
        return

    def on_runtime_disable(self, keyboard):
        return

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def deinit(self, keyboard):
        pass