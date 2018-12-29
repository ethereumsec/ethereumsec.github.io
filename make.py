from clean import deltree
from shutil import move

import os
import subprocess

########################################################################################################################

D = '.'
OUTPUT_PATH = D + os.sep + 'output'
COURSE_PATH = D + os.sep + 'course'
WORKING_COURSE_CONTENT_PATH = COURSE_PATH + os.sep + 'content2'
COURSE_OUTPUT_PATH = D + os.sep + 'course' + os.sep + 'output'
BLOG_SUBPATH = OUTPUT_PATH + os.sep + 'blog'
COURSE_SUBPATH = OUTPUT_PATH + os.sep + 'course'

########################################################################################################################

# Clean away old artifact directories
deltree(OUTPUT_PATH)
deltree(WORKING_COURSE_CONTENT_PATH)
deltree(COURSE_OUTPUT_PATH)

# We'll go ahead and make new output directories now...
os.mkdir(OUTPUT_PATH)
os.mkdir(COURSE_OUTPUT_PATH)

# Make a working content directory .\course\content2 for the course
os.mkdir(WORKING_COURSE_CONTENT_PATH)

# Bring everything up from the subdirectories of the working course content directory
subdirs = [os.path.join(WORKING_COURSE_CONTENT_PATH, o) for o in os.listdir(WORKING_COURSE_CONTENT_PATH) \
                    if os.path.isdir(os.path.join(WORKING_COURSE_CONTENT_PATH,o))]
for subdir in subdirs:
    for filename in os.listdir(subdir):
        if os.path.isfile(os.path.join(subdir, filename)):
            move(os.path.join(subdir, filename), os.path.join(subdir, '..', filename))

# Run `pelican .\course\content2 -t .\theme -o .\course\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'course' + os.sep + 'content2 -t .' + os.sep + 'theme -o .' + os.sep
command_to_run += 'course' + os.sep + 'output -s .' + os.sep + 'pelicanconf.py --relative-urls'
process = subprocess.Popen(command_to_run)
process.wait()

# Run `pelican .\content -t .\theme -o .\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'content -t .' + os.sep + 'theme -o .' + os.sep + 'output -s .'
command_to_run += os.sep + 'pelicanconf.py --relative-urls'
process = subprocess.Popen(command_to_run)
process.wait()

# Move .\course\output\course.html to .\output
move(COURSE_OUTPUT_PATH + 'course.html', OUTPUT_PATH + os.sep + 'course.html')

# Make directory .\output\course
os.mkdir(COURSE_SUBPATH)

# Move all the other HTML files in .\course\output to .\output\course
# TODO does this need to be recursive??
files = os.listdir(COURSE_OUTPUT_PATH)
for file_ in files:
    if file_.endswith('.html') and os.path.isfile(os.path.join(COURSE_OUTPUT_PATH, file_)):
        move(os.path.join(COURSE_OUTPUT_PATH, file_), os.path.join(COURSE_SUBPATH, file_))

# Make directory .\output\blog
os.mkdir(BLOG_SUBPATH)

# Look (non-recursively) at remaining HTML files in .\output...
# TODO

# If filename isn't a "whitelisted" file then put into .\output\blog
html_files_whitelist = ['archives.html', 'authors.html', 'blog.html', 'categories.html', \
                                                                'course.html', 'index.html', 'tags.html']
# TODO
