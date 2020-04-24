# Sen-Making-and-Explanation
This is the dataset for <Does It Make Sense? And Why? A Pilot Study for Sense Making and Explanation> , which has been accepted by ACL-2019.

You can download the paper through https://arxiv.org/abs/1906.00363 .

You can call this dataset as **Sen-Making**.

# Amendent on the Paper
I sincerely apologize for making the 'perplexity' mistake in the paper.

We use score = (p_{1}*p_{2}...p_{n})^{-1/n} =(\prod_{i=1}^{n}(p_{i} | sentence))^{-1/n} to calculate each sentence's score. 
 
We use the probabilities of the all words of one sentence to calculate it.
We didn't think about using perplexity. We only wanted to use p_{i}|(sentence) to design a metric. But after we created the formula, we mistakenly mapped it to perplexity.

We have revised the paper on this mistake, so please read the reversed paper in arXiv https://arxiv.org/abs/1906.00363 rather than the paper in Anthology.

# Data Example
![Example Picture](https://github.com/wangcunxiang/Sen-Making-and-Explanation/raw/master/example.png)
# Data Format
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
## ELMo Baseline

You can find it at https://github.com/Shuailong/bilm-tf.

# SemEval-2020

We will hold a contest in SemEval2020 based on this study. This contest will provide a **Training set** and a **Development set**of these tasks.

You can check task 4 - Commonsense Validation and Explanation in http://alt.qcri.org/semeval2020/index.php?id=tasks.

Looking forward to your participation!

 # Citation
 If you find our work helpful, you can cite
 ```bib
 @inproceedings{wang-etal-2019-make,
    title = "Does it Make Sense? And Why? A Pilot Study for Sense Making and Explanation",
    author = "Wang, Cunxiang  and
      Liang, Shuailong  and
      Zhang, Yue  and
      Li, Xiaonan  and
      Gao, Tian",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1393",
    pages = "4020--4026",
    abstract = "Introducing common sense to natural language understanding systems has received increasing research attention. It remains a fundamental question on how to evaluate whether a system has the sense-making capability. Existing benchmarks measure common sense knowledge indirectly or without reasoning. In this paper, we release a benchmark to directly test whether a system can differentiate natural language statements that make sense from those that do not make sense. In addition, a system is asked to identify the most crucial reason why a statement does not make sense. We evaluate models trained over large-scale language modeling tasks as well as human performance, showing that there are different challenges for system sense-making.",
}
 ```
