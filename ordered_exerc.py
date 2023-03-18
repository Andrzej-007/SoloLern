

from collections import OrderedDict

favorite_lang = OrderedDict()

favorite_lang['andrzej'] = 'python'
favorite_lang['robert'] = 'phisic'
favorite_lang['ivonka'] = 'spanish'
favorite_lang['michal'] = 'informatic'

for name, languges in favorite_lang.items():
    print(f'{name.title()}"s favorite lang. is {languges.title()}')
