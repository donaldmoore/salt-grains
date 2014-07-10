# @author Donald Ray Moore Jr (dmoore@suspectedterrorist.org)
# @purpose salt grain to count redhat packages

import os

def package_update_count():
  return {'package_updates': os.popen("yum check-update | grep -v '^ * ' | wc -l").readline().rstrip()}

  if __name__ == '__main__':
    package_update_count()
