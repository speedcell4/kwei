from aku import Aku

from kwei.dumper import dump

aku = Aku()

aku.register(dump)

aku.run()
