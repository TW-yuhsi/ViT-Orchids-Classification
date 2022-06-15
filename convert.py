import csv
import time

startT = time.time()


dictionary = {'0': 0, '1': 1, '10': 2, '100': 3, '101': 4, '102': 5, '103': 6, '104': 7, '105': 8, '106': 9, '107': 10, '108': 11, '109': 12, '11': 13, '110': 14, '111': 15, '112': 16, '113': 17, '114': 18, '115': 19, '116': 20, '117': 21, '118': 22, '119': 23, '12': 24, '120': 25, '121': 26, '122': 27, '123': 28, '124': 29, '125': 30, '126': 31, '127': 32, '128': 33, '129': 34, '13': 35, '130': 36, '131': 37, '132': 38, '133': 39, '134': 40, '135': 41, '136': 42, '137': 43, '138': 44, '139': 45, '14': 46, '140': 47, '141': 48, '142': 49, '143': 50, '144': 51, '145': 52, '146': 53, '147': 54, '148': 55, '149': 56, '15': 57, '150': 58, '151': 59, '152': 60, '153': 61, '154': 62, '155': 63, '156': 64, '157': 65, '158': 66, '159': 67, '16': 68, '160': 69, '161': 70, '162': 71, '163': 72, '164': 73, '165': 74, '166': 75, '167': 76, '168': 77, '169': 78, '17': 79, '170': 80, '171': 81, '172': 82, '173': 83, '174': 84, '175': 85, '176': 86, '177': 87, '178': 88, '179': 89, '18': 90, '180': 91, '181': 92, '182': 93, '183': 94, '184': 95, '185': 96, '186': 97, '187': 98, '188': 99, '189': 100, '19': 101, '190': 102, '191': 103, '192': 104, '193': 105, '194': 106, '195': 107, '196': 108, '197': 109, '198': 110, '199': 111, '2': 112, '20': 113, '200': 114, '201': 115, '202': 116, '203': 117, '204': 118, '205': 119, '206': 120, '207': 121, '208': 122, '209': 123, '21': 124, '210': 125, '211': 126, '212': 127, '213': 128, '214': 129, '215': 130, '216': 131, '217': 132, '218': 133, '22': 134, '23': 135, '24': 136, '25': 137, '26': 138, '27': 139, '28': 140, '29': 141, '3': 142, '30': 143, '31': 144, '32': 145, '33': 146, '34': 147, '35': 148, '36': 149, '37': 150, '38': 151, '39': 152, '4': 153, '40': 154, '41': 155, '42': 156, '43': 157, '44': 158, '45': 159, '46': 160, '47': 161, '48': 162, '49': 163, '5': 164, '50': 165, '51': 166, '52': 167, '53': 168, '54': 169, '55': 170, '56': 171, '57': 172, '58': 173, '59': 174, '6': 175, '60': 176, '61': 177, '62': 178, '63': 179, '64': 180, '65': 181, '66': 182, '67': 183, '68': 184, '69': 185, '7': 186, '70': 187, '71': 188, '72': 189, '73': 190, '74': 191, '75': 192, '76': 193, '77': 194, '78': 195, '79': 196, '8': 197, '80': 198, '81': 199, '82': 200, '83': 201, '84': 202, '85': 203, '86': 204, '87': 205, '88': 206, '89': 207, '9': 208, '90': 209, '91': 210, '92': 211, '93': 212, '94': 213, '95': 214, '96': 215, '97': 216, '98': 217, '99': 218}


#keys = [k for k, v in dictionary.items() if v == row[1]]
#print(keys)

file = open('./submit_meanEnsemble.csv')    ######## 1. filename ########
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
with open('./submit_meanEnsemble_convert.csv', 'w', newline='') as file:    ######## 2. output name ########
    writer = csv.writer(file)
    writer.writerow(header)
    for row in csvreader:
        #print([k for k, v in dictionary.items() if v == int(row[1])][0])
        row[1] = [k for k, v in dictionary.items() if v == int(row[1])][0]
        writer.writerow(row)

print(time.time() - startT)