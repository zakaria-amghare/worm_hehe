import random,string
def random_name(ext="txt"):
    return "".join(random.choices(string.ascii_lowercase, k=12)) +"."+ ext