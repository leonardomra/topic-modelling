from lda import LDA

class TopicModeller:

    lda = None
    data = None
    target = None
    shouldUseDump = False

    def __init__(self, shouldUseDump):
        self.lda = LDA()
        self.shouldUseDump = shouldUseDump

    def CSV2Topics(self, file):
        self.data = file
        self.target = self.selectTargetColumn('text_body')
        return self.lda.produceTopics(self.target, self.shouldUseDump)
    
    def CSV2TermAmount(self, file):
        self.data = file
        self.target = self.selectTargetColumn('text_body')
        return self.lda.countWords(self.target, self.shouldUseDump)

    def selectTargetColumn(self, columnName):
        return self.data[columnName]