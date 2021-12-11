# Genome Corrector

参考基因组和注释是转录组分析的基础。然而由于技术误差，现有的参考基因组和注释是存在错误的。为了解决这一问题，我们编写了`Genome Corrector`用于更新参考基因组。`Genome Corrector`的输入文件是待更新的参考基因组、待更新的注释文件和用于更新的测序结果；输出文件是更新后的参考基因组和更新后的注释文件。

## 使用方法

打开测试文件所在目录`../Genome_Corrector/test/`，在命令行执行以下命令：
    
    python ../Genome_Corrector test_genome.fa test_annotation.gtf test_sequence.fasta output_genome.fa output_annotation.gtf
    
接收的参数以此为`待更新的参考基因组`、`待更新的注释文件`、`用于更新的测序结果`、`更新后的参考基因组`和`更新后的注释文件`。

## 原理

### makeblastdb

### splign


采用的是屏蔽（以N替代）原有序列并直接添加新序列的策略（可以防止替换出现错误导致基因组错位），进而在添加新注释的时也无需删除原有注释。
