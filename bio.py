
acids = {
    'Ala': [
        'GCA',
        'GCC',
        'GCG',
        'GCU'
    ],
    'Arg': [
        'CGA',
        'CGC',
        'CGG',
        'CGU',
        'AGA',
        'AGG'
    ],
    'Asp': [
        'GAC',
        'GAU'
    ],
    'Asn': [
        'AAC',
        'AAU'
    ],
    'Cys': [
        'UGC',
        'UGU'
    ],
    'Glu': [
        'GAA',
        'GAG'
    ],
    'Gln': [
        'CAA',
        'CAG'
    ],
    'Gly': [
        'GGA',
        'GGC',
        'GGG',
        'GGU'
    ],
    'His': [
        'CAC',
        'CAU'
    ],
    'Ile': [
        'AUA',
        'AUC',
        'AUU'
    ],
    'Leu': [
        'CUA',
        'CUC',
        'CUG',
        'CUU',
        'UUA',
        'UUG'
    ],
    'Lys': [
        'AAA',
        'AAG'
    ],
    'Met': [
        'AUG'
    ],
    'Phe': [
        'UUU',
        'UUC'
    ],
    'Pro': [
        'CCA',
        'CCC',
        'CCG',
        'CCU'
    ],
    'Ser': [
        'UCA',
        'UCC',
        'UCG',
        'UCU',
        'AGC',
        'AGU'
    ],
    'Thr': [
        'ACU',
        'ACC',
        'ACG',
        'ACA'
    ],
    'Trp': [
        'UGG'
    ],
    'Tyr': [
        'UAC',
        'UAU'
    ],
    'Val': [
        'GUA',
        'GUC',
        'GUG',
        'GUU'
    ],
    'STOP': [
        'UAG',
        'UAA',
        'UGA'
    ]
}

names = {
    "Ala": "Alanine",
    "Arg": "Arginine",
    "Asp": "Aspartic acid",
    "Asn": "Asparagine",
    "Cys": "Cysteine",
    "Glu": "Glutamic acid",
    "Gln": "Glutamine",
    "Gly": "Glycine",
    "His": "Histidine",
    "Ile": "Isoleucine",
    "Leu": "Leucine",
    "Lys": "Lysine",
    "Met": "Methionine",
    "Phe": "Phenylalanine",
    "Pro": "Proline",
    "Ser": "Serine",
    "Thr": "Threonine",
    "Trp": "Tryptophan",
    "Tyr": "Tyrosine",
    "Val": "Valine",
    "STOP": "STOP",
}

if __name__ == '__main__':

    # for terminal
    def get_c(string, color):
        '''
        Return the given in string in the given color.
        '''
        colors = {
            'orange': '\033[01;93m',
            'red': '\033[01;91m',
            'green': '\033[01;92m',
            'blue': '\033[01;94m',
            'bold': '\033[01m',
            'dark': '\033[02m',
            'normal': '\033[00m'
        }
        return colors[color] + string + colors['normal']

else:
    # for gui

    def get_c(string, color):
        '''
        Return the given in string in the given color.
        '''

        colors = {
            "grey": "#243160",
            "blue": "#db39b3",
            "orange": "#a17a1a",
            "red": "#d43737"
        }

        if color in colors.keys():
            color = colors[color]

        if color in ['bold', 'dark']:
            return f'<font color="black">{string}</font>'

        return f'<font color="{color}">{string}</font>'

class DNA:

    def __init__(self, strand=None, code=None):
        
        if strand is not None:
            self.strand1 = strand
        
        elif code is not None:
            self.strand1 = Strand(code)

        self.strand2 = strand.complementary()

    def _get_formated_lines(self, left, center, right):

        for i in range(len(center)):
            left_letter = ' '.join(left[i].split(' ')[-2:])
            right_letter = ' '.join(right[i].split(' ')[:2])
            
            center[i] = left_letter + '&#160;&#160;' + center[i] + '&#160;&#160;' + right_letter
            left[i] = ' '.join(left[i].split(' ')[:-2])
            right[i] = ' '.join(right[i].split(' ')[2:])

        return left, center, right

    def display_translated(self, return_lines=False):
        rib1 = Ribose(self.strand1.transcribe())
        rib2 = Ribose(self.strand2.transcribe())

        lines1 = rib1.__str__(side='left', get_lines=True)
        lines2 = rib2.__str__(side='right', get_lines=True)
        lines = self.__str__(get_lines=True)

        if return_lines:
            return self._get_formated_lines(lines1, lines, lines2)

        string = ''

        for left, center, right in zip(lines1, lines, lines2):
            string += f'{left} {center} {right}\n'
        
        print(string)

    def __str__(self, get_lines=False):
        
        lines = []

        for b1, b2 in zip(self.strand1.code, self.strand2.code):
            lines.append( '  ' + get_c(b1 + ' - ' + b2, 'bold') + '  ')
        
        if get_lines:
            return lines
        else:
            return '\n'.join(lines)

class Strand:
    pairs = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C',
    }

    def __init__(self, code, start="5'", end="3'"):
        self.code = code.upper()
        self.start = start
        self.end = end
    
    def transcribe(self):
        strand = self.complementary()

        while 'T' in strand.code:
            strand.code = strand.code.replace('T', 'U')
        
        return strand

    def inv_transcribe(self):
        strand = Strand(self.code, self.start, self.end)
        
        while 'U' in strand.code:
            strand.code = strand.code.replace('U', 'T')

        return strand.complementary()

    def complementary(self):
        '''
        Get the complementary strand,  
        inverse start & end attributes
        '''
        code = ''

        for base in self.code:
            code += self.pairs[base]
        
        return Strand(code, start=self.end, end=self.start)

    def __str__(self):
        return self.code

class Ribose(Strand):
    '''
    Ribose, inherit from Strand.  

    Take a transcribed strand as argument.
    '''

    def __init__(self, strand: Strand):

        self._code = strand.code
        self.start = strand.start
        self.end = strand.end

        self.acids = []

        # for display
        self._st_idx = 0

        self.translate()

    @property
    def code(self):
        if self.start == "5'":
            return self._code
        else:
            return self._code[::-1]

    @code.setter
    def code(self, value):
        if self.start == "5'":
            self._code = value.upper()
        else:
            self._code = value.upper()[::-1]

    def translate(self):

        size = len(self.code)

        self.acids = []

        # look for start
        for i in range(size-2):
            if self.code[i:i+3] == acids['Met'][0]:
                self._st_idx = i
                break
        else:
            self._st_idx = size

        for i in range(self._st_idx, size - 2, 3):
            
            # exceeded end of code
            if i + 3 > size:
                break

            acidname = self._scan(self.code[i:i+3])
            self.acids.append(acidname)

            if acidname == 'STOP':
                break

    def _scan(self, code):
        '''
        Match the given code (length: 3) with one of the acids  
        Return the acid name
        '''
        for acidname, acidcodes in acids.items():
            
            if code in acidcodes:
                # match acid
                return acidname

    def __str__(self, side='right', get_lines=False):

        lines = []
        padding = 15

        for i in range(self._st_idx):
            line = ' ' * (padding)
            
            if side == 'right':
                lines.append(get_c(self.code[i], 'dark') + line)
            else:
                lines.append(line + get_c(self.code[i], 'dark'))
        
        i = self._st_idx
        v = True

        for acid in self.acids:

            if acid == 'Met':
                color = 'green'
            elif acid == 'STOP':
                color = 'red'
            elif v:
                color = 'orange'
            else:
                color = 'blue'

            name = names[acid]

            if side == 'right':
            
                lines.append(get_c(self.code[i], color) + ' ' * (padding))

                line = get_c(self.code[i+1], color) + '  ' + name + ' ' * (padding - len(name) - 2)
                lines.append(line)

                lines.append(get_c(self.code[i + 2], color) + ' ' * (padding))

            else:
                lines.append(' ' * (padding) + get_c(self.code[i], color))

                line = ' ' * (padding - len(name) - 2) + name + '  ' + get_c(self.code[i+1], color) 
                lines.append(line)

                lines.append(' ' * (padding) + get_c(self.code[i + 2], color))

            v = not v
            i += 3

        for i in range(i, len(self.code)):
            line = ' ' * (padding)

            if side == 'right':
                lines.append(get_c(self.code[i], 'dark') + line)
            else:
                lines.append(line + get_c(self.code[i], 'dark'))

        # set lines according to direction of code
        if self.start == "5'":
            lines = lines
        else:
            lines = lines[::-1]

        if get_lines:
            return lines
        else:
            return '\n'.join(lines)


if __name__ == '__main__':
    
    gen0 = 'atgaagttttcttatcgcttataa'
    gen1 = 'atgaagttttcatatcgcttataa'
    gen2 = 'atgaagtttgcttatcgcttataa'

    strand = Strand(gen1)#, start="3'", end="5'")

    DNA(strand).display_translated()

    
