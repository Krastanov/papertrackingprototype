import yaml
import pprint

pprint.pprint(yaml.load(open("test.yaml").read(), Loader=yaml.Loader))
