class BruteForceGenerator:
    ENGLISH_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    GREEK_LETTERS = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'ά', 'έ', 'ή', 'ί', 'ό', 'ύ', 'ώ', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'ϊ', 'ϋ', 'Ϊ', 'Ϋ', 'ΐ', 'ΰ', 'Ί', 'Ύ', '΄', '¨']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*','(', ')', '-', '_', '=', '+', ';', ':', '/', '\\', '?', '€', '.', ',', '<', '>', '"', '\'', '|', ' ']

    def __init__(self, vocabulary: list, max_length = 10):
        self.vocabulary = vocabulary
        self.max_length = max_length
        self.count_list = list()
        for _ in range(0, max_length):
            self.count_list.append(0)

    def generateNext(self):
        self.count_list[len(self.count_list) - 1] += 1

        for i in range(len(self.count_list) - 1, 0, -1):
            if self.count_list[i] == len(self.vocabulary) + 1:
                self.count_list[i - 1] += 1
                self.count_list[i] = 1

        if self.count_list[0] == len(self.vocabulary)+1:
            # Reached max, starting all over again
            for i in range(0, len(self.count_list)-1):
                self.count_list[i] = 0
            self.count_list[len(self.count_list) - 1] = 1

        return self.generateCurrent()

    def generateCurrent(self):
        tempWord = ""
        for i in self.count_list:
            if i == 0:
                continue
            try:
                tempWord += self.vocabulary[i - 1]
            except IndexError:
                    pass
        return tempWord

    @staticmethod
    def generateList(vocabulary: list, max_length: int):
        tempGenerator = BruteForceGenerator(vocabulary, max_length+1)
        toReturn = list()
        while len(tempGenerator.generateNext()) <= max_length:
            toReturn.append(tempGenerator.generateCurrent())
        return toReturn
