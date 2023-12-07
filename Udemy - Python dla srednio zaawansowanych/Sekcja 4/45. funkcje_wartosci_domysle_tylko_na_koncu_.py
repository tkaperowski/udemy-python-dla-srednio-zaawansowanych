def BuyMe(prefix='default PREFIX', what='default WHAT'):
    print(prefix, what)



BuyMe('My PREFIX value', 'My WHAT value')
BuyMe('My PREFIX value')
BuyMe(prefix="podaje nazwe parametru PREFiX")
BuyMe('abc', what="podaje nazwe parametru PREFiX")

# argumenty z wartościami domyslnymi muszą być na końcu listy
def ArgumentyZwartosciaNaKoncu(prefix, what='default WHAT'):
    print(prefix, what)


ArgumentyZwartosciaNaKoncu("abc")

# argumenty z wartościami dimyślnymi nie mogą być przez agrumentami bez wartości domyślnych, kompilator nie pozwoli
# na taką funkcję bo nie wie gdzie wstawić argument z wywołania funkcji:
# def ArgumentBezWartosciNaKonce(prefix='default PREFIX', what):
#     print("my what")
#
# ArgumentBezWartosciNaKonce("test")

# WNIOSEK: jeśli wymagamy podania swoich argumentow to definiuj je na początku funkji