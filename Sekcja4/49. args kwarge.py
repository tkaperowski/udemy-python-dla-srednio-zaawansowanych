def calculate_paint(efficency_ltr_per_m2, *args):
    args = sum(args)
    result = efficency_ltr_per_m2 * args
    print(f'ilosc litrów = {result}')

calculate_paint(1, 2, 2, 10)

lista_pokoi = [2, 2, 10]
calculate_paint(1, *lista_pokoi)


def log_it(*args):
    print(args)
    # args = str(args)
    with open(r'd:\Udemy\log_it2.txt', 'a') as f:
        for i in args:
            print(i)
            f.write(i + ' ')
        f.write('\n')

# zapisz = r'd:\Udemy\log_it.txt'
log_it("abc")
log_it('222')
log_it('xyz', '123')
log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

with open(r'd:\Udemy\log_it2.txt', 'r') as f:
    print(f.read())