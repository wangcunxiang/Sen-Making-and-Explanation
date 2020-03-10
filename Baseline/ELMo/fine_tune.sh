# @Author: Liang Shuailong <handsome>
# @Date:   2019-02-01T15:22:37+08:00
# @Last modified by:   handsome
# @Last modified time: 2019-02-01T15:36:11+08:00

export CUDA_VISIBLE_DEVICES=1

python bin/restart.py \
    --save_dir models/checkpoint \
    --vocab_file models/vocab-2016-09-10.txt \
    --train_prefix "/data/additional_corpus.txt" \
    --n_gpus 1 \
    --batch_size 128 \
    --n_train_tokens 768648884 \
    --n_epochs 5
