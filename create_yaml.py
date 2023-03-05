import yaml

wheet_yaml = dict(
    train ='D:/globalwheet/Dataset/train',
    val ='D:/globalwheet/Dataset/val',
    test='D:/globalwheet/Dataset/test',
    nc =1,
    names =["wheat"]
)

with open('wheet.yaml', 'w') as outfile:
    yaml.dump(wheet_yaml, outfile, default_flow_style=True)