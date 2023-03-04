

def show_magicitis(magic_names):

    for i in magic_names:
        print(i)

def make_great(magic_names, the_grate_name):

    for i in magic_names:
        # print(f"i : {i}")
        the_grate_name.append(f"the_great_{i}")
    # print(f"chech test: {magic_names}")


magic_names = ['and', 'rob', 'iwo', 'jago']
the_grate_name =[]
show_magicitis(magic_names)
make_great(magic_names, the_grate_name)

print(the_grate_name)





