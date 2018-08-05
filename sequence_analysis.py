import matplotlib.pyplot as plt
class Sequence(object):
    def __init__(self, sequence):
        self.sequence = sequence
        self.codes = ['a','r','n','d','c',
                      'e','q','g','h','i',
                      'l','k','m','f','p',
                      's','t','w','y','v']
        self.acids = ['alanine','arginine','asparagine','aspartic acid','cysteine',
                      'glutamic acid','glutamine','glycine','histidine','isoleucine',
                      'leucine','lysine','methionine','phenylalanine','proline',
                      'serine','threonine','tryptophan','tyrosine','valine']
        # 0 is nonpolar, 1 is polar, 2 is acidic, 3 is basic
        self.type = [0,3,1,2,1,
                     2,1,0,3,0,
                     0,3,0,0,0,
                     1,1,0,1,0]
        # 0 is aliphatic, 1 is Sulfur, 2 is cyclic, 3 is aromatic, 4 is basic, 5 is acidic
        self.classtype = [0,4,5,5,1,
                          5,5,0,4,0,
                          0,4,1,3,2,
                          1,1,3,3,0]
        #0 is charged, 1 is polar, 2 is hydrophobic
        self.interaction = [2,0,1,0,1,
                             0,1,2,1,2,
                             2,0,2,2,2,
                             1,1,1,1,2]

    def translate(self):
        names = []
        k = 0
        for i in self.sequence:
            for j in range(len(self.codes)):
                if i == self.codes[j]:
                    k = j
            names.append(self.acids[k])
        return names

    def get_frequencies(self):
        frequencies = [0,0,0,0,0,
                       0,0,0,0,0,
                       0,0,0,0,0,
                       0,0,0,0,0]
        k = 0
        for i in self.sequence:
            for j in range(len(self.codes)):
                if i == self.codes[j]:
                    k = j
            frequencies[k] += 1
        return frequencies

    def get_type(self):
        types = []
        k = 0
        for i in self.sequence:
            for j in range(len(self.codes)):
                if i == self.codes[j]:
                    k = j
            types.append(self.type[k])
        return types

    def get_typefreqs(self):
        types = self.get_type()
        numbers = [0, 0, 0, 0]
        for i in types:
            numbers[i] += 1
        numbers = [numbers[i] / len(types) for i in range(len(numbers))]
        return numbers

    def get_classtype(self):
        classtypes = []
        k = 0
        for i in self.sequence:
            for j in range(len(self.codes)):
                if i == self.codes[j]:
                    k = j
            classtypes.append(self.classtype[k])
        return classtypes

    def get_classtypefreqs(self):
        classtypes = self.get_classtype()
        numbers = [0, 0, 0, 0, 0, 0]
        for i in classtypes:
            numbers[i] += 1
        numbers = [numbers[i] / len(classtypes) for i in range(len(numbers))]
        return numbers

    def get_interactions(self):
        interactions = []
        k = 0
        for i in self.sequence:
            for j in range(len(self.codes)):
                if i == self.codes[j]:
                    k = j
            interactions.append(self.interaction[k])
        return interactions

    def get_interactfreqs(self):
        interactions = self.get_interactions()
        numbers = [0, 0, 0]
        for i in interactions:
            numbers[i] += 1
        numbers = [numbers[i] / len(interactions) for i in range(len(numbers))]
        return numbers

    def plot_types(self):
        numbers = self.get_typefreqs()
        labels = ['Nonpolar', 'Polar', 'Acidic', 'Basic']
        plt.pie(numbers, labels=labels)
        plt.show()

    def plot_classtypes(self):
        numbers = self.get_classtypefreqs()
        labels = ['Aliphatic', 'Hydroxyl/Sulfur','Cyclic',
                  'Aromatic', 'Basic', 'Acidic+Amide']
        plt.pie(numbers, labels=labels)
        plt.show()

    def plot_interactions(self):
        numbers = self.get_interactfreqs()
        labels = ['Charged', 'Polar', 'Hydrophobic']
        plt.pie(numbers, labels=labels)
        plt.show()

def pre_format(filename):
    file = open(filename, 'r')
    vals = []
    for line in file:
        line = list(line)
        for i in line:
            if i != "\n" and i != " ":
                vals.append(i)
    return vals

filename = 'dna_polymerase.txt'
codes = pre_format(filename)
sequencer = Sequence(codes)
names = sequencer.translate()
frequencies = sequencer.get_frequencies()
print(frequencies)
sequencer.plot_types()
numbers = sequencer.get_typefreqs()
print(numbers)
