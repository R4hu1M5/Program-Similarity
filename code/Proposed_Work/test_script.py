import sys
import pickle

program_number1 = sys.argv[1]
filename_prognum = "program"+program_number1

output_file_lev1_pc = open((filename_prognum+"_lev1_pc.pickle"), "rb")
pc_1 = pickle.load(output_file_lev1_pc)

output_file_lev2_pc = open((filename_prognum+"_lev2_pc.pickle"), "rb")
pc_2 = pickle.load(output_file_lev2_pc)

# for ele in pc_1:
#     print(ele, "\n")

for ele in pc_2:
    print(ele, "\n")
