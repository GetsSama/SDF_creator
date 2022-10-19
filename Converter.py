import SeqToSDF
import json


path_to_config = "config\\1000.json"

with open(path_to_config, 'r') as config:
    properties = config.read()

prop_dict = json.loads(properties)

path_to_peptides = "C:\\Users\\Zh_Nikolay\\Desktop\\peptides\\"

def config_redactor(number):
    peptide_file_name = "pept_" + str(number) + ".csv"
    print("\nCurrent file: " + peptide_file_name)
    input_property = path_to_peptides + peptide_file_name
    prop_dict["input"] = input_property
    new_json = json.dumps(prop_dict)

    with open(path_to_config, 'w') as config:
        config.write(new_json)


def start():
    for i in range(15):
        config_redactor(i+1)
        SeqToSDF.start_fun(path_to_config)


if __name__ == '__main__':
    start()
