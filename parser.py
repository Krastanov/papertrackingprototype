import yaml
import pprint
import glob

for f in glob.glob('./content/*'):
    print(f)
    try:
        metadata = open(f+"/README.md").read().split('---')[1]
        pprint.pprint(yaml.load(metadata, Loader=yaml.Loader))
    except:
        print("AAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH")
    print("")

