from glob import glob

NMI_INDEX = 6
ARI_INDEX = 9
CA_INDEX = 12
JAC_INDEX = 15

EXPECTED_K = 2


for filename in glob("files/*.csv"):
    with open(filename, "r") as f:
        lines = list(map(lambda x:x.replace("\n", "").split(","), f.readlines()))[2:]

    tuples = []
    for thing in zip(["4-NMI", "3-ARI", "1-CA", "2-Jac"], [NMI_INDEX, ARI_INDEX, CA_INDEX, JAC_INDEX]):
        count = list(filter(lambda x: x[EXPECTED_K] == x[thing[1]], lines))
        datasets = set(list(map(lambda x:x[0], count)))
        for dataset in datasets:
            row_count = len(list(filter(lambda x:x[0] == dataset, count)))
            for _ in range(row_count):
                tuples.append((dataset, thing[0], str(row_count)))
    out_str = "\n".join(list(map(lambda x:", ".join(x), tuples)))
    with open("out/" + "".join(filename.replace("\\", "/").split("/")[1:]), "w") as f:
        f.write(out_str)

#print("\n".join(list(map(lambda x:", ".join(x), NMI_count))))
