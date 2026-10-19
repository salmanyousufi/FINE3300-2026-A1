import csv

class ExchangeRates:
    def __init__(self, filename):
        self.fx_val = 0.0
        rates_file = open(filename, 'r')
        reader_obj = csv.DictReader(rates_file)
        for entry in reader_obj:
            if entry['FXAUSDCAD'] != '':
                self.fx_val = float(entry['FXAUSDCAD'])
        rates_file.close()

    def convert(self, money, curr_from, curr_to):
        c_from = curr_from.strip().upper()
        c_to = curr_to.strip().upper()
        
        if c_from == 'USD' and c_to == 'CAD':
            return money * self.fx_val
        elif c_from == 'CAD' and c_to == 'USD':
            return money / self.fx_val
        elif c_from == c_to:
            return money
        else:
            return None