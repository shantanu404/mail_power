def get(filepath):
    usrname = pass_ = ""
    with open(filepath) as f:
        content = f.read()
        info = content.split('|')
        return (info[0], info[1])
