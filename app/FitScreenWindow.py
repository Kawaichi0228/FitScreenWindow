#! /usr/bin/env python3.9

# ===============================================================================
# - FitScreenWindow -
#
# Copyright (C) Kawaichi0228
# ===============================================================================
#import src.fitscreenwindowapp as app
from src.lib.config import ConfigJsonRepository

#gui_service = app.GuiService()
#gui_service.start()

#app.main()

json = ConfigJsonRepository()
print(json.HotkeyWindowRight.mod_ctrl)