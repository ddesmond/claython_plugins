# SETUP THE OSL NODE IN SELECTED CONTEXT
import ix
import os

claython_plugin_path = os.path.normpath(str(os.getenv("CLAYTHON_PATH")+"/claython_core/claython_plugins/misc/osl_simplex_noise/osl_simplex_noise.osl"))

current_context = ix.get_current_context()

with open(claython_plugin_path) as f:
    contents = f.read()


osl_item = ix.cmds.CreateObject("OSL_simplex_noise", "TextureOslScript", "Global", current_context)
print osl_item
inject_item = str(str(osl_item)+".OSL_shader_script")

ix.cmds.SetValues([inject_item], [contents])