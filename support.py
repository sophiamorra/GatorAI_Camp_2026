from os import walk, path
import pygame

def import_folder(folder_path):
	"""Load every image in a folder and return them as a list of surfaces."""
	surface_list = []
	base_path = path.dirname(path.abspath(__file__))

	for _, __, img_files in walk(path.join(base_path, folder_path)):
		for image in sorted(img_files):
			full_path = path.join(base_path, folder_path, image)
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def import_folder_dict(folder_path):
	"""Load every image in a folder into a dict keyed by filename (without extension)."""
	surface_dict = {}
	base_path = path.dirname(path.abspath(__file__))

	for _, __, img_files in walk(path.join(base_path, folder_path)):
		for image in img_files:
			full_path = path.join(base_path, folder_path, image)
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_dict[image.split('.')[0]] = image_surf

	return surface_dict


# @STUDENT-EDIT-Day2-7: You've just read two real FUNCTIONS above (import_folder and
# import_folder_dict). Now write your OWN! A function has: a `def` line with a name and
# inputs, a docstring, indented code, and (usually) a `return`. Try writing:
#
#   def add(x, y):
#       '''Take two values and return their sum.'''
#       return x + y
#
# Then call it - add(3, 4) should give 7. Challenge: write square(n) that returns n ** 2.
# (You can practice functions in scratch.py too.)