import csv
from collections import defaultdict, namedtuple


def read_csv(path):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        IncidentTuple = namedtuple('IncidentTuple', next(reader))
        for r in reader:
            data.append(IncidentTuple(*r))
    return data


def get_all_category_with_id(data):
    dd = defaultdict(lambda: defaultdict(str))
    for d in data:
        di = d._asdict()
        for k in di.keys():
            if '代碼' in k and k not in ['發生地址_路街代碼', '發生地址_村里代碼']:
                k1 = k
                k2 = k.replace('代碼', '名稱')
                v1 = di[k1]
                v2 = di[k2]
                if v1 == ' ':
                    continue

                if v2 in ['營業用', '自用']:
                    v2 += di[k2.replace('子類', '大類')]
                dd[k1][v1] = v2
    return dd


def get_all_keys(data):
    keys = data[0]._asdict().keys()
    return list(filter(
        lambda x: False if ('名稱' in x and
                            x.replace('名稱', '代碼') in keys) else True, keys))


def jsonify(data):
    keys = data[0]._asdict().keys()
    kk = list(filter(
        lambda x: False if ('名稱' in x and
                            x.replace('名稱', '代碼') in keys) else True, keys))
    v = []
    for d in data:
        v.append({k: v for k, v in d._asdict().items() if k in kk})
    return v


if __name__ == '__main__':
    import sys
    data = read_csv(sys.argv[1])
    d = data[0]._asdict()
    v = get_all_keys(data)
    for i in v:
        try:
            int(d[i])
            print(i, '= db.Column(db.Integer)')
        except:
            print(i, '= db.Column(db.String(10))')
