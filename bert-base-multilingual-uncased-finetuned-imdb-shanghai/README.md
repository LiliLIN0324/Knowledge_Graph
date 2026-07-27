---
license: apache-2.0
base_model: bert-base-multilingual-uncased
tags:
- generated_from_trainer
model-index:
- name: bert-base-multilingual-uncased-finetuned-imdb-shanghai
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-uncased-finetuned-imdb-shanghai

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5883

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.41.2
- Pytorch 2.7.1+cpu
- Datasets 3.6.0
- Tokenizers 0.19.1
