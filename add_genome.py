def add_genome(sequence_file):
    f = open(sequence_file, 'r')
    a = f.readlines()
    f.close()
    f = open('mask_result.txt', 'a')
    f.writelines('\n')
    f.writelines(a)
    f.close()