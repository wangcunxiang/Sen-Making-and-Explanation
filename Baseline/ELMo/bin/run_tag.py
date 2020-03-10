import os
import argparse
from glob import glob

from bilm.training import tag, load_options_latest_checkpoint, load_vocab
from bilm.data import LMDataset, BidirectionalLMDataset

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'

def main(args):
    print(args)
    print('-' * 100)
    print('Loading models and options...')
    options, ckpt_file = load_options_latest_checkpoint(args.save_dir)
    print('Loading vocabulary...')
    # load the vocab
    if 'char_cnn' in options:
        max_word_length = options['char_cnn']['max_characters_per_token']
    else:
        max_word_length = None
    vocab = load_vocab(args.vocab_file, max_word_length)

    shards = glob(args.test_prefix)
    shards.sort()
    # print(shards)
    kwargs = {
        'test': True,
        'shuffle_on_load': False,
    }
    print(f'Building dataset...')
    datasets = []
    for shard in shards:
        if options.get('bidirectional'):
            datasets.append(BidirectionalLMDataset(shard, vocab, **kwargs))
        else:
            datasets.append(LMDataset(shard, vocab, **kwargs))

    print('Predicting...')
    tag(options, ckpt_file, shards, datasets, batch_size=args.batch_size)
    print('-' * 100)
    print('done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute test perplexity')
    parser.add_argument('--save_dir', help='Location of checkpoint files')
    parser.add_argument('--vocab_file', help='Vocabulary file')
    parser.add_argument('--test_prefix', help='test prefix')
    parser.add_argument('--batch_size',
        type=int, default=1,
        help='Batch size')

    args = parser.parse_args()
    main(args)
