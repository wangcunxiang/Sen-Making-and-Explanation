# @Author: Liang Shuailong <handsome>
# @Date:   2019-01-29T13:54:11+08:00
# @Last modified by:   handsome
# @Last modified time: 2019-02-01T14:21:29+08:00
export CUDA_VISIBLE_DEVICES=1

python bin/run_tag.py \
    --test_prefix="data/cs*" \
    --vocab_file models/vocab-2016-09-10.txt \
    --save_dir models/checkpoint \
    --batch_size 1
