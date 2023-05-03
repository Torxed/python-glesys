import importlib
import sys
import pathlib

"""
This logic is here to allow for relative imports via the .git repo,
as well as installed versions as a backup.
"""
if pathlib.Path('./glesys/__init__.py').absolute().exists():
	spec = importlib.util.spec_from_file_location("glesys", "./glesys/__init__.py")
	glesys = importlib.util.module_from_spec(spec)
	sys.modules["glesys"] = glesys
	spec.loader.exec_module(sys.modules["glesys"])
else:
	import glesys

if __name__ == '__main__':
	glesys.run_as_a_module()