import json


def get_folders(array):
    folders = []
    for index in array:
        if index["type"] == "folder":
            folders.append(index)
    return folders


def check_parents(data, array):
    parents = []
    for item in array:
        parents.append()


def main(inputFile, outputFile):
    with open(inputFile, 'r') as input:
        data = json.load(input)
    folders = get_folders(data)
    parents = check_parents(data, folders)
    with open(outputFile, 'w') as output:
        json.dump(folders,  output, sort_keys=True,
                  indent=4)


if __name__ == "__main__":
    main("inputJson.json", "outputJson.json")
