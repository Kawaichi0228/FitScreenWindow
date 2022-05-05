#! /usr/bin/env python3.9

# ===============================================================================
# - FitScreenWindow -
#
# Copyright (C) Kawaichi0228
# ===============================================================================
#import src.fitscreenwindowapp as app
from src.lib.config import JsonRepository

#gui_service = app.GuiService()
#gui_service.start()

#app.main()

json = JsonRepository(r"\app\src\config.json")
print(json.Size.is_subtract_taskbar)