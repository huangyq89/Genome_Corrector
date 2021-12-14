# Genome Corrector

参考基因组和注释是转录组分析的基础。然而由于技术误差，现有的参考基因组和注释是存在错误的。为了解决这一问题，我们编写了`Genome Corrector`用于更新参考基因组。`Genome Corrector`的输入文件是待更新的参考基因组、待更新的注释文件和用于更新的测序结果；输出文件是更新后的参考基因组和更新后的注释文件。

## 使用方法

在Linux命令行执行：

    git clone https://github.com/huangyq89/Genome_Corrector.git

打开测试文件所在目录`../Genome_Corrector/test/`，在命令行执行以下命令：
    
    python ../Genome_Corrector test_genome.fa test_annotation.gtf test_sequence.fasta output_genome.fa output_annotation.gtf
    
接收的参数依次为`待更新的参考基因组`、`待更新的注释文件`、`用于更新的测序结果`、`更新后的参考基因组`和`更新后的注释文件`。

## 原理

`Genome Corrector`首先调用自带的`splign`（下载自NCBI），确定用于更新的测序结果在参考基因组中的位置，并生成`output.splign`文件；接下来`mask.py`根据`output.splign`中的结果屏蔽（以N替代）参考基因组中原有的序列；最后`add_genome.py`在参考基因组末尾添加新序列，`add_annotation.py`在注释文件末尾添加新序列的注释。
