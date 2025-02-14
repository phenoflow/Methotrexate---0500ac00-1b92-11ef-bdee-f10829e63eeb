# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"36849","system":"gprdproduct"},{"code":"46039","system":"gprdproduct"},{"code":"28041","system":"gprdproduct"},{"code":"35752","system":"gprdproduct"},{"code":"27404","system":"gprdproduct"},{"code":"36800","system":"gprdproduct"},{"code":"40301","system":"gprdproduct"},{"code":"59723","system":"gprdproduct"},{"code":"27400","system":"gprdproduct"},{"code":"40280","system":"gprdproduct"},{"code":"17035","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('methotrexate-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["methotrexate-m3-015ml---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["methotrexate-m3-015ml---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["methotrexate-m3-015ml---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
