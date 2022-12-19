import re
import os
import pathlib
import PySimpleGUI as sg


path = sg.popup_get_folder("Select a Folder")
if not path:
	sg.popup("Cancel", "No Folder Selectd")
	raise SystemExit("Cancelled: No Folder Selected")
else:
	sg.popup("The Folder You Selected Was", path)

os.chdir(path)
folder = pathlib.Path('.')

def remove_anime_tags(folder):
	regex = r"\[(.+)?\] "
	subst = ""
	for file in folder.iterdir():
		if file.is_file():
			name,ext = os.path.splitext(file)
			striped = re.sub(regex, subst, name, 3, re.IGNORECASE)
			new_name = f"{striped}{ext}"
			file.rename(new_name)
			sg.popup(f"Changed{file} to {new_name}")
			

if __name__ == "__main__":
	remove_anime_tags(folder)