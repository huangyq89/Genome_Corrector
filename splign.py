import os

def splign(genome, sequence_file):
    os.system('mkdir execute_splign')
    sentence = 'cp ' + sequence_file + ' ' + genome + ' execute_splign'
    os.system(sentence)
    os.system('../splign -mklds execute_splign')
    os.system('../makeblastdb -dbtype nucl -parse_seqids -in execute_splign/' + sequence_file)
    os.system('../makeblastdb -dbtype nucl -parse_seqids -in execute_splign/' + genome)
    os.system('../compart -qdb execute_splign/' + sequence_file + ' -sdb execute_splign/' + genome + ' > output.compartments')
    os.system('../splign -ldsdir execute_splign -comps output.compartments > output.splign')

