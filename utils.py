"""
utils functions
"""
def get_credentials(filepath):
    """Gets the user credentials from a file"""
    with open(filepath) as credentials:
        content = credentials.read()
        info = content.split('|')
        return (info[0], info[1])
