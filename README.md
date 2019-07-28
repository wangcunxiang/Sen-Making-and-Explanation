# Sen-Making-and-Explanation
This is the dataset for <Does It Make Sense? And Why? A Pilot Study for Sense Making and Explanation> , which has been accepted by ACL-2019.

You can download the paper through https://arxiv.org/abs/1906.00363 .
# Data Format
### TXT Sample
```txt
id : 1
sentence0 : he put an elephant into the fridge
sentence1 : he put a turkey into the fridge
false : 0
A : an elephant is much bigger than a fridge
B : elephants are usually gray while fridges are usually white
C : an elephant cannot eat a fridge
reason : A
```
### JSON Sample
```json
{
  "id": "1", 
  "sentence0": "he put an elephant into the fridge", 
  "sentence1": "he put a turkey into the fridge", 
  "false": 0, 
  "A": "an elephant is much bigger than a fridge", 
  "B": "elephants are usually gray while fridges are usually white", 
  "C": "an elephant cannot eat a fridge", 
  "reason": "A"
}
 ```
 # Citation
 If you find our work helpful, you can cite
 ```bib
 @article{DBLP:journals/corr/abs-1906-00363,
  author    = {Cunxiang Wang and
               Shuailong Liang and
               Yue Zhang and
               Xiaonan Li and
               Tian Gao},
  title     = {Does It Make Sense? And Why? {A} Pilot Study for Sense Making and
               Explanation},
  journal   = {CoRR},
  volume    = {abs/1906.00363},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.00363},
  archivePrefix = {arXiv},
  eprint    = {1906.00363},
  timestamp = {Thu, 13 Jun 2019 13:36:00 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1906-00363},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
# SemEval-2020
We will hold a contest in SemEval2020 based on this study. 
You can check task 4 in http://alt.qcri.org/semeval2020/index.php?id=tasks
Looking forward to your participation.
You can find a more detailed task decription on https://www.youtube.com/watch?v=UAcO1I97iWg
