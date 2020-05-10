#!/usr/bin/env python3
import argparse, docker, os, platform, shutil, stat, time
from os.path import exists, expanduser, join


# Retrieves the list of aliases exported by a Docker container image (if any)
def listAliases(image):
	labels = image.attrs['Config']['Labels'] if image.attrs['Config']['Labels'] is not None else {}
	return list(sorted([labels[key] for key in labels if key.startswith('developer-images.aliases.')]))

# Repeatedly calls a function until it succeeds or the max number of retries has been reached
def repeat(func, maxRetries=5, sleepTime=0.5):
	for i in range(0, maxRetries):
		try:
			func()
			break
		except Exception as error:
			if i == maxRetries - 1:
				raise error from None
			else:
				time.sleep(sleepTime)

# Ensures that the specified directory exists and is empty
# (The removal step can sometimes fail arbitrarily under Windows, so we repeat it if necessary)
def truncateDir(dir):
	if exists(dir):
		repeat(lambda: shutil.rmtree(dir))
	os.makedirs(dir)

# Writes data to a file
def write(filename, data):
	with open(filename, 'wb') as f:
		f.write(data.encode('utf-8'))


# Parse our command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('outdir', metavar='OUTDIR', nargs='?', default=expanduser('~/.devimage-aliases'), help='The output directory for the generated aliases (defaults to ~/.devimage-aliases)')
args = parser.parse_args()

# Ensure the output directory exists, deleting any existing aliases
truncateDir(args.outdir)

# Iterate over each of the Docker images on the system and identify the images that export aliases
client = docker.from_env()
for image in client.images.list():
	aliases = listAliases(image)
	if len(image.tags) > 0 and len(aliases) > 0:
		
		# Print progress output
		tag = image.tags[0]
		print('Processing aliases for image "{}":'.format(tag))
		
		# Generate an alias file for each alias the image exports
		for alias in aliases:
			
			# Determine if the alias just exposes a command of the same name or if it specifies a mapping
			components = alias.split('=', 1)
			source = components[0] if len(components) > 1 else alias
			target = components[1] if len(components) > 1 else alias
			
			# Print progress output
			print('    Generating alias "{}" for "{}"...'.format(source, target))
			
			# Generate an appropriate script for the host platform
			if platform.system().lower() == 'windows':
				
				# Generate a .cmd file under Windows
				write(join(args.outdir, '{}.cmd'.format(source)), '@docker-shell {} {} -- %*'.format(target, tag))
				
			else:
				
				# Generate an extensionless shell script under Linux and macOS
				script = join(args.outdir, source)
				write(script, '#!/usr/bin/env bash\ndocker-shell {} {} -- "$@"'.format(target, tag))
				os.chmod(script, os.stat(script).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
