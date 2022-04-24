import os
import sys
from datetime import datetime

import yaml
from kaggle import api

start = datetime.strptime(sys.argv[1], "%Y-%m-%d")
end = datetime.strptime(sys.argv[2], "%Y-%m-%d")

comps = api.competitions_list(page=2)
filepath = os.path.abspath(os.path.dirname(sys.argv[0]))
filepath = "/".join(os.path.split(filepath)[:-1])
with open(f"{filepath}/_data/competitions.yml") as fin:
    config = yaml.load(fin, Loader=yaml.FullLoader)
i = int(config["competitions"][0]["number"])
for comp in comps:
    deadline = getattr(comp, "deadline")
    if start.date() < deadline.date() and deadline.date() < end.date():
        i += 1
with open(f"{os.environ['HOME']}/Desktop/new.txt", "w") as fout:
    for comp in comps:
        deadline = getattr(comp, "deadline")
        if start.date() < deadline.date() and deadline.date() < end.date():
            title = comp.title.replace(":", ";").replace("'", "")
            desc = comp.description.replace(":", ";").replace("'", "")
            kind = comp.category
            prize = comp.reward
            team = comp.teamCount
            try:
                team = "{:,}".format(int(team))
            except Exception:
                team = "-"
            metric = comp.evaluationMetric
            if metric is not None and len(metric) > 0:
                metric = metric.replace(":", ";").replace("'", "")
            else:
                metric = "-"
            link = f"https://www.kaggle.com/c/{comp.ref}"
            image = "https://storage.googleapis.com/kaggle-competitions/kaggle/---/logos/thumb76_76.png"
            year = deadline.year
            isHot = "false"
            done = "false"
            print(f"  - number: '{i}'", file=fout)
            print(f"    title: '{title}'", file=fout)
            print(f"    desc: '{desc}'", file=fout)
            print(f"    kind: '{kind}'", file=fout)
            print(f"    prize: '{prize}'", file=fout)
            print(f"    team: '{team}'", file=fout)
            print(f"    metric: '{metric}'", file=fout)
            print(f"    link: '{link}'", file=fout)
            print(f"    image: '{image}'", file=fout)
            print(f"    year: '{year}'", file=fout)
            print(f"    isHot: '{isHot}'", file=fout)
            print(f"    done: '{done}'", file=fout)
            print("    solutions: ", file=fout)
            for _ in range(3):
                print("      - rank: ''", file=fout)
                print("        link: ''", file=fout)
                print("        kind: 'description'", file=fout)
            i -= 1
