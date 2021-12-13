from mask import *
from add_genome import *
from add_annotation import *
import sys

# 接收的参数依次为待更新的参考基因组、待更新的注释文件、用于更新的测序结果、更新后的参考基因组和更新后的注释文件
splign(sys.argv[3])
mask(sys.argv[1])
add_genome(sys.argv[3], sys.argv[4])
add_annotation(sys.argv[2], sys.argv[5])

