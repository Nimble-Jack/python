#Answer:
# https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary

#%%
def group_by_owners(files):
    last_name = dict()
    for file in files.items():
        if file[1] in last_name:
            last_name[file[1]].append(file[0])
        else:
            last_name[file[1]] = [file[0]]
    print(last_name)
#%%
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
group_by_owners(files)


'''
Example of how dictionaries work
'''
#%%
test = dict()
test['john'] = ['mik']
test['john'].append('lol')
#%%
test