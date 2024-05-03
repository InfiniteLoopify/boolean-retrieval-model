from indexer.index import Indexer
from indexer.gui import Table

if __name__ == "__main__":
    indexer = Indexer()
    indexer.read_file("speech/")
    indexer.index_to_file("files/")

    tb = Table()
    tb.create_Gui(indexer)
