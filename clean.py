import os

def deltree(target):
    if False == os.path.exists(target):
        return
    for d in os.listdir(target):
        try:
            deltree(target + os.sep + d)
            os.rmdir(target + os.sep + d)
        except OSError:
            os.remove(target + os.sep + d)
    try:
        os.rmdir(target)
    except:
        pass

if __name__ == '__main__':
    deltree('.' + os.sep + 'output')
    deltree('.' + os.sep + 'course' + os.sep + 'content2')
    deltree('.' + os.sep + 'course' + os.sep + 'output')
