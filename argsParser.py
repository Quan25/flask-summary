import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('str2bool value expected.')


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-accum_count", type=int)
    parser.add_argument("-alpha", type=float)
    parser.add_argument("-batch_size", type=int)
    parser.add_argument("-beam_size", type=int)
    parser.add_argument("-bert_data_path")
    parser.add_argument("-beta1", type=float)
    parser.add_argument("-beta2", type=float)
    parser.add_argument("-block_trigram", type=str2bool)
    parser.add_argument("-dec_dropout", type=float)
    parser.add_argument("-dec_ff_size", type=int)
    parser.add_argument("-dec_heads", type=int)
    parser.add_argument("-dec_hidden_size", type=int)
    parser.add_argument("-dec_layers", type=int)
    parser.add_argument("-enc_dropout", type=float)
    parser.add_argument("-enc_ff_size", type=int)
    parser.add_argument("-enc_hidden_size", type=int)
    parser.add_argument("-enc_layers", type=int)
    parser.add_argument("-encoder", type=str)
    parser.add_argument("-ext_dropout", type=float)
    parser.add_argument("-ext_ff_size",type=int)
    parser.add_argument("-ext_heads", type=int)
    parser.add_argument("-ext_hidden_size", type=int)
    parser.add_argument("-ext_layers", type=int)
    parser.add_argument("-finetune_bert", type=str2bool)
    parser.add_argument("-generator_shard_size", type=int)
    parser.add_argument("-gpu_ranks", type=str)
    parser.add_argument("-label_smoothing", type=float)
    parser.add_argument("-large", type=str2bool)
    parser.add_argument("-load_from_extractive", type=str)
    parser.add_argument("-log_file")
    parser.add_argument("-lr", type=float)
    parser.add_argument("-lr_bert", type=float)
    parser.add_argument("-lr_dec", type=float)
    parser.add_argument("-max_grad_norm", type=float)
    parser.add_argument("-max_length", type=int)
    parser.add_argument("-max_ndocs_in_batch", type=int)
    parser.add_argument("-max_pos", type=int)
    parser.add_argument("-max_tgt_len", type=int)
    parser.add_argument("-min_length", type=int)
    parser.add_argument("-mode", type=str)
    parser.add_argument("-model_path")
    parser.add_argument("-optim", type=str)
    parser.add_argument("-param_init", type=float)
    parser.add_argument("-param_init_glorot", type=str2bool)
    parser.add_argument("-recall_eval", type=str2bool)
    parser.add_argument("-report_every", type=int)
    parser.add_argument("-report_rouge", type=str2bool)
    parser.add_argument("-result_path")
    parser.add_argument("-save_checkpoint_steps", type=int)
    parser.add_argument("-seed", type=int)
    parser.add_argument("-sep_optim", type=str2bool)
    parser.add_argument("-share_emb", type=str2bool)
    parser.add_argument("-task", type=str)
    parser.add_argument("-temp_dir")
    parser.add_argument("-test_all", type=str2bool)
    parser.add_argument("-test_batch_size", type=int)
    parser.add_argument("-test_from")
    parser.add_argument("-test_start_from", type=int)
    parser.add_argument("-text_src")
    parser.add_argument("-text_tgt")
    parser.add_argument("-train_from")
    parser.add_argument("-train_steps", type=int)
    parser.add_argument("-use_bert_emb", type=str2bool)
    parser.add_argument("-use_interval", type=str2bool)
    parser.add_argument("-visible_gpus", type=str)
    parser.add_argument("-warmup_steps", type=int)
    parser.add_argument("-warmup_steps_bert", type=int)
    parser.add_argument("-warmup_steps_dec", type=int)
    parser.add_argument("-world_size", type=int)

    test = "-accum_count 1 -alpha 0.6 -batch_size 140 -beam_size 5 -bert_data_path PreSumm/bert_data_new/cnndm -beta1 0.9 -beta2 0.999 -block_trigram True -dec_dropout 0.2 -dec_ff_size 2048 -dec_heads 8 -dec_hidden_size 768 -dec_layers 6 -enc_dropout 0.2 -enc_ff_size 512 -enc_hidden_size 512 -enc_layers 6 -encoder bert -ext_dropout 0.2 -ext_ff_size 2048 -ext_heads 8 -ext_hidden_size 768 -ext_layers 2 -finetune_bert True -generator_shard_size 32 -gpu_ranks [0] -label_smoothing 0.1 -large False -load_from_extractive '' -log_file PreSumm/logs/cnndm.log -lr 1 -lr_bert 0.002 -lr_dec 0.002 -max_grad_norm 0 -max_length 150 -max_ndocs_in_batch 6 -max_pos 512 -max_tgt_len 140 -min_length 15 -mode test_text -model_path PreSumm/models/ -optim adam -param_init 0 -param_init_glorot True -recall_eval False -report_every 1 -report_rouge True -result_path PreSumm/results/cnndm -save_checkpoint_steps 5 -seed 666 -sep_optim False -share_emb False -task abs -temp_dir PreSumm/temp -test_all False -test_batch_size 200 -test_from PreSumm/models/model_step_148000.pt -test_start_from -1 -text_src PreSumm/raw_data/temp.raw_src -text_tgt '' -train_from '' -train_steps 1000 -use_bert_emb False -use_interval True -visible_gpus -1 -warmup_steps 8000 -warmup_steps_bert 8000 -warmup_steps_dec 8000 -world_size 1"

    args = parser.parse_args(test.split())
    args.gpu_ranks = [int(i) for i in range(len(args.visible_gpus.split(',')))]
    args.load_from_extractive = ''
    args.text_tgt = ''
    args.train_from = ''
    args.lr=1
    args.max_grad_norm=0
    args.param_init=0

    return args

    def textFormatter(originalText):
    	processText=""
    	formattedText=''
    	processText = ''.join([line for line in originalText.splitlines() if line.strip()])
    	for each in processText.split('.'):
    		if(each != ''):
    			if(each[0] == ' '):
    				formattedText += each[1:] + '.\n'
    			else:
    				formattedText += each + '.\n'
    	return formattedText
