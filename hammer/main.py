import argparse

from version import __version__

def parse():
    parser = argparse.ArgumentParser(
        description="Hammer - The most orgranized search engine\
                               made by the community\
                               for the community."
        )
    parser.add_argument("--v", action="version", version=__version__)
"""
    parser.add_argument()
    This is a template, just incase we need to use it alot
"""       

null = 0
def search_online():
    
  #  return query

    pass

def search_offline():
    # User's will be able to save information on their computer 
    # and will be able to search it offline
  #  return offlineQuery
  pass

def main():

    pass

if __name__ == "__main__":
    main()
