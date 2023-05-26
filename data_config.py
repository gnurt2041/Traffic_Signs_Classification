## classes.names ##

classes = [
    'car',
    'person',
    'motorcycle',
    'Speed_limit_30km',
    'Speed_limit_40km',
    'Speed_limit_50km',
    'Speed_limit_60km',
    'Speed_limit_70km',
    'Speed_limit_80km',
    'Speed_limit_90km',
    'Speed_limit_100km',
    'Speed_limit_110km',
    'Speed_limit_120km',
    'Traffic_light_green',
    'Traffic_light_red',
    'Bend_to_right',
    'Bend_to_left',
    'Double_bend_right',
    'Double_bend_left',
    'No_right_turn',
    'No_left_turn',
    'No_u_turn',
    'No_entry',
    'Narrow_road',
    'Fork_road'
]
## signs_data.yaml ##
num_classes = len(classes)
print(num_classes)
config = {
    'train': '/content/drive/MyDrive/Traffic_Sign_Classification/dataset/train',
    'val': '/content/drive/MyDrive/Traffic_Sign_Classification/dataset/valid',
    'nc': num_classes,
    'names': classes,
}
f = open(f'signs_data.yaml', 'w+')
for key in config:
    f.write(f'{key}: {config[key]}\n')
f.close()
