##################################################
# Program: save
##################################################

##################################################
# System Module Imports
##################################################

##################################################
# Add-In Module Imports
##################################################

##################################################
# Local Module Imports
##################################################
import Qt.Manager as manager
##################################################
# Constant Variable Definitions
##################################################

##################################################
# Global Variable Definitions
##################################################


def save_file_with_dialogue(get_env='HOME'):
    app = manager.get_main_window()
    if app is None:
        return
    return app.save_file(get_env)