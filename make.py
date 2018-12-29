from clean import deltree

import os

# Clean away old artifact directories
deltree('.' + os.sep + 'output')
deltree('.' + os.sep + 'course' + os.sep + 'content2')
deltree('.' + os.sep + 'course' + os.sep + 'output')

# Make a working content directory .\course\content2 for the course
# TODO

# Bring everything up from the subdirectories of the working course content directory
# TODO

# Run `pelican .\course\content2 -t .\theme -o .\course\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'course' + os.sep + 'content2 -t .' + os.sep + 'theme -o .' + os.sep
command_to_run += 'course' + os.sep + 'output -s .' + os.sep + 'pelicanconf.py --relative-urls'
# TODO

# Run `pelican .\content -t .\theme -o .\output -s .\pelicanconf.py --relative-urls`
command_to_run = 'pelican .' + os.sep + 'content -t .' + os.sep + 'theme -o .' + os.sep + 'output -s .'
command_to_run += os.sep + 'pelicanconf.py --relative-urls'
# TODO

# Move .\course\output\course.html to .\output
# TODO

# Make directory .\output\course
# TODO

# Move all the other HTML files in .\course\output to .\output\course
# TODO

# Make directory .\output\blog
# TODO

# Look (non-recursively) at remaining HTML files in .\output...
# TODO

# If filename isn't a "whitelisted" file then put into .\output\blog
html_files_whitelist = ['archives.html', 'authors.html', 'blog.html', 'categories.html', \
                                                                'course.html', 'index.html', 'tags.html']
# TODO
