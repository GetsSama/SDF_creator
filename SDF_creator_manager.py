import os

work_dir = "source_data"
seq_data_dir = "sequence_source"
seq_main_result = "peptides_source"
seq_negative_result = "negative_sample"

if not os.path.exists(work_dir):
    os.mkdir(work_dir)
    os.mkdir(work_dir + "/" + seq_data_dir)
    os.mkdir(work_dir + "/" + seq_main_result)
    os.mkdir(work_dir + "/" + seq_negative_result)