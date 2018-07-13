import matplotlib.pyplot as plt

class PinyinPlotter:
    text = None
    accents = None
    plot_step = 1
    last_y = 0
    last_x = 0
    tone_counts = {'1':0,'2':0,'3':0,'4':0}
    word_count = 0

    def parse_text(self, t_in):
        self.text = t_in.strip().lower()
        self.word_count = len(self.text.split(" "))

    def get_tones(self):
        self.accents = []
        for letter in self.text:
            letter_m = self.identify_m(letter)
            if letter_m != None:
                self.accents.append(letter_m)

    def identify_m(self, tone):
        if tone in 'āēīōūü':
            return [0,0]
        if tone in 'áéíóúǘ':
            return [1,1]
        if tone in 'ǎěǐǒǔǚ':
            return [-2,2]
        if tone in 'àèìòùǜ':
            return [-1,-1]

    def plot_pinyin(self):
        tone1, tone2, tone3, tone4 = (0, 0, 0, 0)
        self.tone_counts = {'1':0,'2':0,'3':0,'4':0}
        self.last_x = 0
        self.last_y = 0
        for tone in self.accents:
            if tone[0] == 0:
                tone_color = (0,0,1)
                self.tone_counts['1'] += 1
            if tone[0] == 1:
                tone_color = (0,1,0)
                self.tone_counts['2'] += 1
            if tone[0] == -2:
                tone_color = (1,0,0)
                self.tone_counts['3'] += 1
            if tone[0] == -1:
                tone_color = (1,0,1)
                self.tone_counts['4'] += 1
            for step in tone:
                x1 = self.last_x
                y1 = self.last_y
                x2 = x1 + self.plot_step
                y2 = (step * (x2-x1)) + y1
                plt.plot([x1,x2],[y1,y2],'-', color = tone_color)
                self.last_x = x2
                self.last_y = y2
        total_accents = len(self.accents)
        try:
            tone1 = 100 * self.tone_counts['1']/total_accents
            tone2 = 100 * self.tone_counts['2']/total_accents
            tone3 = 100 * self.tone_counts['3']/total_accents
            tone4 = 100 * self.tone_counts['4']/total_accents
        except ZeroDivisionError:
            print("No tones found!")

        plt.show()
        print(f"Total words: {self.word_count}")
        print(f"Tone counts: {self.tone_counts}")
        print(f"Proportions: {round(tone1,2)}, {round(tone2,2)}, {round(tone3,2)}, {round(tone4,2)}")


    def do_it_all(self, text):
        self.parse_text(text)
        self.get_tones()
        self.plot_pinyin()
