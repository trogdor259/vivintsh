import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Take a json file and converted to nested json")

    parser.add_argument('-i', '--input_file', type=str, default="inputJson.json",
                        help="The file to convert to nested json")
    parser.add_argument('-o', '--output_file', type=str, default="outputJson.json",
                        help="The file to output the nested json to")
    args = parser.parse_args()

    return args


def get_primary(data):
    names = [item["name"] for item in data]
    parents = [item["parent"] for item in data]
    for parent in parents:
        if parent not in names:
            return parent


def get_names(data):
    return [item["name"] for item in data]


def set_main_folder(data, primary):
    for item in data:
        if item["parent"] == primary and item["type"] == "folder":
            item.update({"children": []})
            return item


def set_children(data, names, primary):
    folders = set_main_folder(data, primary)
    for i in data:
        if i["parent"] in names:
            parent_name = i["parent"]
            for x in data:
                if x["name"] == parent_name and "children" not in x and x["type"] == "folder":
                    x.update({"children": []})
                if x["name"] == parent_name and "children" in x:
                    object = x["children"]
                    object.append(i)
                    x.update({"children": object})
    return folders


def main():
    args = parse_args()
    with open(args.input_file, 'r') as input:
        data = json.load(input)
    primary = get_primary(data)
    folders = set_children(data, get_names(data), primary)
    with open(args.output_file, 'w') as output:
        json.dump(folders,  output, sort_keys=True,
                  indent=4)


if __name__ == "__main__":
    main()
