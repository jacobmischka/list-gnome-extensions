#!/usr/bin/env python3

from os import path, scandir
import json
from argparse import ArgumentParser

METADATA_FILE = 'metadata.json'

def read_dirs(dirs):
	if isinstance(dirs, str):
		dirs = [dirs]

	extension_list = []

	for directory in dirs:
		for extension in scandir(directory):
			if extension.is_dir():
				extension_metadata_file = path.join(extension.path, METADATA_FILE)
				if path.exists(extension_metadata_file):
					with open(extension_metadata_file) as f:
						extension_metadata = json.load(f)
					extension_metadata['installation_location'] = directory
					extension_list.append(extension_metadata)

	return extension_list

def filter_fields(extensions, args):
	if args.all:
		return extensions
	else:
		fields = args.fields if args.fields else ['name']
		return [{field: extension[field] for field in fields} for extension in extensions]


def main():

	parser = ArgumentParser(description='List currently installed gnome extensions.')
	parser.add_argument('-n', '--name', dest='fields', action='append_const', const='name', help='Display extension names (default)')
	parser.add_argument('-u', '--url', dest='fields', action='append_const', const='url', help='Display extension URLs')
	parser.add_argument('-d', '--desc', '--description', dest='fields', action='append_const', const='description', help='Display extension descriptions')
	parser.add_argument('-l', '--location', dest='fields', action='append_const', const='installation_location', help='Display extension installation locations')
	parser.add_argument('-i', '--uuid', dest='fields', action='append_const', const='uuid', help='Display extension UUIDs')
	parser.add_argument('-a', '--all', dest='all', action='store_true', help='Dump all extension metadata')
	parser.add_argument('--group', dest='group', action='store_true', help='Group extensions by installation location')

	extension_directories = [
		'/usr/share/gnome-shell/extensions',
		path.expanduser('~/.local/share/gnome-shell/extensions')
	]

	args = parser.parse_args()

	if args.group:
		output = []
		for ext_dir in extension_directories:
			output.append({'location': ext_dir, 'extensions': filter_fields(read_dirs(ext_dir), args)})
	else:
		output = filter_fields(read_dirs(extension_directories), args)

	print(json.dumps(output, indent=4, sort_keys=True))

if __name__ == '__main__':
	main()
