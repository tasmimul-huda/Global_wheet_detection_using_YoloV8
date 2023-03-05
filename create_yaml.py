import yaml

wheat_yaml = dict(
    train ='D:/globalwheet/Dataset/train',
    val ='D:/globalwheet/Dataset/val',
    test='D:/globalwheet/Dataset/test',
    nc =1,
    names =["wheat"]
)

with open('wheat.yaml', 'w') as outfile:
    yaml.dump(wheat_yaml, outfile, default_flow_style=True)