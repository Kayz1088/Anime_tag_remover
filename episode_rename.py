import re
import os
import pathlib
os.chdir(input("folder location: "))
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
			print(f"Changed{file} to {new_name}")
			

if __name__ == "__main__":
	remove_anime_tags(folder)