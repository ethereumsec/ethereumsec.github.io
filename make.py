from clean import deltree
from shutil import copy, copytree, copy2, move

import glob
import os
import subprocess

########################################################################################################################

D = '.'
OUTPUT_PATH = D + os.sep + 'output'
COURSE_PATH = D + os.sep + 'course'
ORIGIN_COURSE_CONTENT_PATH = COURSE_PATH + os.sep + 'content'
WORKING_COURSE_CONTENT_PATH = ORIGIN_COURSE_CONTENT_PATH + '2'
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

# Recursively find all Markdown files in .\course\content and copy (at root) to .\course\content2
for filepath in glob.iglob(ORIGIN_COURSE_CONTENT_PATH + os.sep + '**' + os.sep + '*.md', recursive=True):
    filename = filepath.split(os.sep)[-1]
    copy(filepath, WORKING_COURSE_CONTENT_PATH + os.sep + filename)

# Run `pelican .\course\content2 -t .\theme -o .\course\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'course' + os.sep + 'content2 -t .' + os.sep + 'theme -o .' + os.sep
command_to_run += 'course' + os.sep + 'output -s .' + os.sep + 'pelicanconf.py --relative-urls'
process = subprocess.Popen(command_to_run)
process.wait()

# Clean up what we don't need now in working course content output
deltree(COURSE_OUTPUT_PATH + os.sep + 'author')
deltree(COURSE_OUTPUT_PATH + os.sep + 'category')
deltree(COURSE_OUTPUT_PATH + os.sep + 'tag')
deltree(COURSE_OUTPUT_PATH + os.sep + 'theme')

# Run `pelican .\content -t .\theme -o .\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'content -t .' + os.sep + 'theme -o .' + os.sep + 'output -s .'
command_to_run += os.sep + 'pelicanconf.py --relative-urls'
process = subprocess.Popen(command_to_run)
process.wait()

# Move .\course\output\course.html to .\output
move(COURSE_OUTPUT_PATH + os.sep + 'course.html', OUTPUT_PATH + os.sep + 'course.html')

# Make directory .\output\course
os.mkdir(COURSE_SUBPATH)

# Copy everything in .\course\output to .\output\course
# FIXME this needs to use glob.iglob and go recursive I think
for item in os.listdir(COURSE_OUTPUT_PATH):
    s = os.path.join(COURSE_OUTPUT_PATH, item)
    d = os.path.join(COURSE_SUBPATH, item)
    if os.path.isdir(s):
        copytree(s, d)
    else:
        copy2(s, d)

# Make directory .\output\blog
os.mkdir(BLOG_SUBPATH)

# Look (non-recursively) at remaining HTML files in .\output...
# If filename isn't a "whitelisted" file then put into .\output\blog
html_files_whitelist = ['archives.html', 'authors.html', 'blog.html', 'categories.html', \
                                                                'course.html', 'index.html', 'tags.html']
for filepath in glob.iglob(OUTPUT_PATH + os.sep + '*.html', recursive=False):
    filename = filepath.split(os.sep)[-1]
    if filename not in html_files_whitelist:
        move(filepath, BLOG_SUBPATH + os.sep + filename)

# Clean again
deltree(WORKING_COURSE_CONTENT_PATH)
deltree(COURSE_OUTPUT_PATH)
