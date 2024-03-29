__author__ = 'carlo'
RND = 3141
SBLEACH = 3
EBLEACH = 1
IBLEACH = 1


def tupler(x):
    return [(bit,)+tup for bit in (0, 1) for tup in tupler(x-1)] if x else [(0,), (1,)]


class Cortex:
    """Discriminador da Rede neural sem peso. :ref:`wisard'
    """
    def __init__(self, retinasize=3*4, bleach=0, ramorder=2):
        # self.cortex = [{t: 0 for t in tupler(ramorder-1)} for _ in range(retinasize//2)]
        self.cortex = [{(a, b): 0 for a in [0, 1] for b in [0, 1]} for _ in range(retinasize//2)]
        self.bleach = bleach

    def learn(self, retina, offset=1):
        def updater(ram, index):
            return {index: self.cortex[ram][index]+offset}
        # print(len(retina)//2)
        x = (len(retina)//2)
        [self.cortex[ram].update(updater(ram, (retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))))
         for ram in range(x)]

    def classify(self, retina):
        x = (len(retina)//2)
        return ([self.cortex[ram][(retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))]-self.bleach
                for ram in range(x)])


class Lobe:
    """Rede neural sem peso. :ref:`enplicaw`

    :param data: input data stream.
    :param topvalue: the largest value of any data.
    :param factor: retina reduction factor to speed up processing.
    :param ramorder: number obits adressing the RAM.
    :param enforce_supress: tuple with one value to offset leraning and a negative to suppress.
    :param bleach: dictionary of bleaches {classkey: bleach_value}
    """

    def __init__(self, data, topvalue, factor=1, ramorder=2, enforce_supress=(1, 0), bleach={k: 0 for k in range(6)}):
        self.retinasize, self.data = len(data), data
        self.l, self.m, self.n = range(len(self.data))[::-1], range(len(self.data[0][0])), range(len(self.data[0]))
        l, m, n = self.l, self.m, self.n
        self.cortex = {key: Cortex(self.retinasize, bleacher) for key, bleacher in bleach.items()}
        self.enforce, self.supress = enforce_supress
        self.bleach = bleach
        self.cortex_keys = sorted(class_key for class_key in bleach.keys())
        self.sample_entries = [[[self.data[i][j][k] for k in m] for i in l] for j in n]
    """Rede neural sem peso. :ref:`wisard'
    """
    def __init__(self, retinasize=3*4, bleach=0, ramorder=2):
        # self.cortex = [{t: 0 for t in tupler(ramorder-1)} for _ in range(retinasize//2)]
        self.cortex = [{(a, b): 0 for a in [0, 1] for b in [0, 1]} for _ in range(retinasize//2)]
        self.bleach = bleach

    def learn(self, retina, offset=1):
        def updater(ram, index):
            return {index: self.cortex[ram][index]+offset}
        # print(len(retina)//2)
        x = (len(retina)//2)
        [self.cortex[ram].update(updater(ram, (retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))))
         for ram in range(x)]

    def classify(self, retina):
        x = (len(retina)//2)
        return ([self.cortex[ram][(retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))]-self.bleach
                for ram in range(x)])


DATA = '''
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5.0,3.6,1.4,0.2,Iris-setosa
5.4,3.9,1.7,0.4,Iris-setosa
4.6,3.4,1.4,0.3,Iris-setosa
5.0,3.4,1.5,0.2,Iris-setosa
4.4,2.9,1.4,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
5.4,3.7,1.5,0.2,Iris-setosa
4.8,3.4,1.6,0.2,Iris-setosa
4.8,3.0,1.4,0.1,Iris-setosa
4.3,3.0,1.1,0.1,Iris-setosa
5.8,4.0,1.2,0.2,Iris-setosa
5.7,4.4,1.5,0.4,Iris-setosa
5.4,3.9,1.3,0.4,Iris-setosa
5.1,3.5,1.4,0.3,Iris-setosa
5.7,3.8,1.7,0.3,Iris-setosa
5.1,3.8,1.5,0.3,Iris-setosa
5.4,3.4,1.7,0.2,Iris-setosa
5.1,3.7,1.5,0.4,Iris-setosa
4.6,3.6,1.0,0.2,Iris-setosa
5.1,3.3,1.7,0.5,Iris-setosa
4.8,3.4,1.9,0.2,Iris-setosa
5.0,3.0,1.6,0.2,Iris-setosa
5.0,3.4,1.6,0.4,Iris-setosa
5.2,3.5,1.5,0.2,Iris-setosa
5.2,3.4,1.4,0.2,Iris-setosa
4.7,3.2,1.6,0.2,Iris-setosa
4.8,3.1,1.6,0.2,Iris-setosa
5.4,3.4,1.5,0.4,Iris-setosa
5.2,4.1,1.5,0.1,Iris-setosa
5.5,4.2,1.4,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
5.0,3.2,1.2,0.2,Iris-setosa
5.5,3.5,1.3,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
4.4,3.0,1.3,0.2,Iris-setosa
5.1,3.4,1.5,0.2,Iris-setosa
5.0,3.5,1.3,0.3,Iris-setosa
4.5,2.3,1.3,0.3,Iris-setosa
4.4,3.2,1.3,0.2,Iris-setosa
5.0,3.5,1.6,0.6,Iris-setosa
5.1,3.8,1.9,0.4,Iris-setosa
4.8,3.0,1.4,0.3,Iris-setosa
5.1,3.8,1.6,0.2,Iris-setosa
4.6,3.2,1.4,0.2,Iris-setosa
5.3,3.7,1.5,0.2,Iris-setosa
5.0,3.3,1.4,0.2,Iris-setosa
7.0,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
6.9,3.1,4.9,1.5,Iris-versicolor
5.5,2.3,4.0,1.3,Iris-versicolor
6.5,2.8,4.6,1.5,Iris-versicolor
5.7,2.8,4.5,1.3,Iris-versicolor
6.3,3.3,4.7,1.6,Iris-versicolor
4.9,2.4,3.3,1.0,Iris-versicolor
6.6,2.9,4.6,1.3,Iris-versicolor
5.2,2.7,3.9,1.4,Iris-versicolor
5.0,2.0,3.5,1.0,Iris-versicolor
5.9,3.0,4.2,1.5,Iris-versicolor
6.0,2.2,4.0,1.0,Iris-versicolor
6.1,2.9,4.7,1.4,Iris-versicolor
5.6,2.9,3.6,1.3,Iris-versicolor
6.7,3.1,4.4,1.4,Iris-versicolor
5.6,3.0,4.5,1.5,Iris-versicolor
5.8,2.7,4.1,1.0,Iris-versicolor
6.2,2.2,4.5,1.5,Iris-versicolor
5.6,2.5,3.9,1.1,Iris-versicolor
5.9,3.2,4.8,1.8,Iris-versicolor
6.1,2.8,4.0,1.3,Iris-versicolor
6.3,2.5,4.9,1.5,Iris-versicolor
6.1,2.8,4.7,1.2,Iris-versicolor
6.4,2.9,4.3,1.3,Iris-versicolor
6.6,3.0,4.4,1.4,Iris-versicolor
6.8,2.8,4.8,1.4,Iris-versicolor
6.7,3.0,5.0,1.7,Iris-versicolor
6.0,2.9,4.5,1.5,Iris-versicolor
5.7,2.6,3.5,1.0,Iris-versicolor
5.5,2.4,3.8,1.1,Iris-versicolor
5.5,2.4,3.7,1.0,Iris-versicolor
5.8,2.7,3.9,1.2,Iris-versicolor
6.0,2.7,5.1,1.6,Iris-versicolor
5.4,3.0,4.5,1.5,Iris-versicolor
6.0,3.4,4.5,1.6,Iris-versicolor
6.7,3.1,4.7,1.5,Iris-versicolor
6.3,2.3,4.4,1.3,Iris-versicolor
5.6,3.0,4.1,1.3,Iris-versicolor
5.5,2.5,4.0,1.3,Iris-versicolor
5.5,2.6,4.4,1.2,Iris-versicolor
6.1,3.0,4.6,1.4,Iris-versicolor
5.8,2.6,4.0,1.2,Iris-versicolor
5.0,2.3,3.3,1.0,Iris-versicolor
5.6,2.7,4.2,1.3,Iris-versicolor
5.7,3.0,4.2,1.2,Iris-versicolor
5.7,2.9,4.2,1.3,Iris-versicolor
6.2,2.9,4.3,1.3,Iris-versicolor
5.1,2.5,3.0,1.1,Iris-versicolor
5.7,2.8,4.1,1.3,Iris-versicolor
6.3,3.3,6.0,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
7.1,3.0,5.9,2.1,Iris-virginica
6.3,2.9,5.6,1.8,Iris-virginica
6.5,3.0,5.8,2.2,Iris-virginica
7.6,3.0,6.6,2.1,Iris-virginica
4.9,2.5,4.5,1.7,Iris-virginica
7.3,2.9,6.3,1.8,Iris-virginica
6.7,2.5,5.8,1.8,Iris-virginica
7.2,3.6,6.1,2.5,Iris-virginica
6.5,3.2,5.1,2.0,Iris-virginica
6.4,2.7,5.3,1.9,Iris-virginica
6.8,3.0,5.5,2.1,Iris-virginica
5.7,2.5,5.0,2.0,Iris-virginica
5.8,2.8,5.1,2.4,Iris-virginica
6.4,3.2,5.3,2.3,Iris-virginica
6.5,3.0,5.5,1.8,Iris-virginica
7.7,3.8,6.7,2.2,Iris-virginica
7.7,2.6,6.9,2.3,Iris-virginica
6.0,2.2,5.0,1.5,Iris-virginica
6.9,3.2,5.7,2.3,Iris-virginica
5.6,2.8,4.9,2.0,Iris-virginica
7.7,2.8,6.7,2.0,Iris-virginica
6.3,2.7,4.9,1.8,Iris-virginica
6.7,3.3,5.7,2.1,Iris-virginica
7.2,3.2,6.0,1.8,Iris-virginica
6.2,2.8,4.8,1.8,Iris-virginica
6.1,3.0,4.9,1.8,Iris-virginica
6.4,2.8,5.6,2.1,Iris-virginica
7.2,3.0,5.8,1.6,Iris-virginica
7.4,2.8,6.1,1.9,Iris-virginica
7.9,3.8,6.4,2.0,Iris-virginica
6.4,2.8,5.6,2.2,Iris-virginica
6.3,2.8,5.1,1.5,Iris-virginica
6.1,2.6,5.6,1.4,Iris-virginica
7.7,3.0,6.1,2.3,Iris-virginica
6.3,3.4,5.6,2.4,Iris-virginica
6.4,3.1,5.5,1.8,Iris-virginica
6.0,3.0,4.8,1.8,Iris-virginica
6.9,3.1,5.4,2.1,Iris-virginica
6.7,3.1,5.6,2.4,Iris-virginica
6.9,3.1,5.1,2.3,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
6.8,3.2,5.9,2.3,Iris-virginica
6.7,3.3,5.7,2.5,Iris-virginica
6.7,3.0,5.2,2.3,Iris-virginica
6.3,2.5,5.0,1.9,Iris-virginica
6.5,3.0,5.2,2.0,Iris-virginica
6.2,3.4,5.4,2.3,Iris-virginica
5.9,3.0,5.1,1.8,Iris-virginica
'''.split()
MAP = {"Iris-virginica": 0, "Iris-versicolor": 1, "Iris-setosa": 2}
SDATA = {0: [], 1: [], 2: []}
[SDATA[MAP[r.split(",")[-1]]].append([int(float(d)*10)
 for d in r.split(",")[:-1]]) for r in DATA]
print (SDATA)
print("#"*20)
FATOR = 4
ZFATOR = 2*FATOR
TOP = 100//FATOR
BDATA = {i: [[([0]*(1*(j//ZFATOR)))+([1]*(j//ZFATOR))+([0]*(TOP-(2*(j//ZFATOR))))
              for j in k] for k in d] for i, d in SDATA.items()}
# BDATA = {i: [[[1]*j for j in k] for k in d] for i, d in SDATA.items()}
print(BDATA)
print("#"*40)
print ([["".join("%d" % i for i in j) for j in k] for k in BDATA[0][:10]])
# print ([1 for j in BDATA[0][0]  for i in j] )
RS = (sum(1 for j in BDATA[0][0] for i in j))


def go():
    setosa = Wisard(RS, SBLEACH)
    versicolor = Wisard(RS, EBLEACH)
    virginica = Wisard(RS, IBLEACH)
    dse = BDATA[2][:]
    dve = BDATA[1][:]
    dvi = BDATA[0][:]
    from random import shuffle
    shuffle(dse)
    shuffle(dve)
    shuffle(dvi)
    ENFORCE = 9
    SUPPRESS = -4
    for i in range(5):
        lse, lve, lvi = dse.pop(),  dve.pop(), dvi.pop()
        setosa.learn([i for j in lse for i in j], ENFORCE)
        versicolor.learn([i for j in lve for i in j], ENFORCE)
        virginica.learn([i for j in lvi for i in j], ENFORCE)
        setosa.learn([i for j in lve for i in j], SUPPRESS)
        versicolor.learn([i for j in lvi for i in j], SUPPRESS)
        virginica.learn([i for j in lse for i in j], SUPPRESS)
        setosa.learn([i for j in lvi for i in j], SUPPRESS)
        versicolor.learn([i for j in lse for i in j], SUPPRESS)
        virginica.learn([i for j in lve for i in j], SUPPRESS)
    # print("#"*20)
    # print(setosa.cortex)
    for i in []:
        rse, rve, rvi = dse.pop(),  dve.pop(), dve.pop()
        setosa.classify([i for j in rse for i in j])
        versicolor.learn([i for j in rve for i in j])
        virginica.learn([i for j in rvi for i in j])

    cls = [
        [
            sorted([
                (sum(setosa.classify([i for j in rse for i in j])), 0),
                (sum(versicolor.classify([i for j in rse for i in j])), 1),
                (sum(virginica.classify([i for j in rse for i in j])), 2)
            ]),
            sorted([
                (sum(setosa.classify([i for j in rve for i in j])), 0),
                (sum(versicolor.classify([i for j in rve for i in j])), 1),
                (sum(virginica.classify([i for j in rve for i in j])), 2)
            ]),
            sorted([
                (sum(virginica.classify([i for j in rvi for i in j])), 2),
                (sum(versicolor.classify([i for j in rvi for i in j])), 1),
                (sum(setosa.classify([i for j in rvi for i in j])), 0)
            ])
        ] for rse, rve, rvi in zip(dse, dve, dvi)]

    # print (cls)
    ocls = [[(tup[-1][1], 100*(tup[-1][0] - tup[-2][0])//tup[-1][0]) for tup in triade] for triade in cls]
    # print(ocls)
    scls = [[1 for clsd, real in zip(cl, (0, 1, 2)) if clsd[0] == real] for cl in ocls]
    sscls = sum(1 for cl in ocls for clsd, real in zip(cl, (0, 1, 2)) if clsd[0] == real)
    # print(scls)
    return 100*sscls//(len(scls)*3)
SAMP = 500
acc = [go() for _ in range(SAMP)]

print(min(acc), max(acc), sum(acc)//SAMP)  # , acc)
