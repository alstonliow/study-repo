---
title: "Transfer Learning and Fine-Tuning"
sources: [cs231n-11, cs231na-3]
requires: [ai/deep-learning/pooling-and-cnn-architectures]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Transfer learning: feature extraction, fine-tuning, when and how to fine-tune, practical advice) and Assignment 3 (linear probes on pretrained features), in our own wording. -->

Few tasks come with a million labelled images. *Transfer learning* reuses a network trained on a large dataset (the *source* task, usually ImageNet classification, or a self-supervised task, @sec-ai-unsupervised-learning-contrastive-learning) for a new *target* task with less data.

::: {#def-transfer-learning .definition name="Feature extraction and fine-tuning"}

Let a pretrained network be split as $f=h\circ\boldsymbol\phi$: a *backbone* $\boldsymbol\phi$ (all layers up to the last hidden layer) and a *head* $h$ (the final classifier).

1. *Feature extraction* (a *linear probe* when the new head is linear): keep $\boldsymbol\phi$ fixed, compute the codes $\boldsymbol\phi(\mathbf{x}_i)$ of the target data once, and train only a new head on them, for example a softmax classifier (@def-softmax).
2. *Fine-tuning*: replace the head, initialize the backbone with the pretrained weights, and continue training all (or only the later) layers on the target data by backpropagation.

:::

Early layers compute generic features (edges, colours, textures) that transfer to almost any image task; later layers are increasingly specific to the source classes. This decides how much to retrain.

::: {#rmk-transfer-learning-cases .remark name="Which variant to use"}

| target data | similar to the source | different from the source |
|---|---|---|
| small | linear classifier on the last codes; fine-tuning would overfit | linear classifier on codes from an earlier layer |
| large | fine-tune the whole network | fine-tune the whole network, or train from scratch, still often initialized from the pretrained weights |

:::

::: {#rmk-transfer-learning-practice .remark name="Practical points"}

1. Fine-tune with a learning rate about ten times smaller than for training from scratch, often with an even smaller one for the backbone than for the new head: the pretrained weights are already good and should move little.
2. A frequent recipe trains the new head first with the backbone frozen, then unfreezes and fine-tunes everything.
3. The pretrained architecture constrains the input. Convolutional layers accept larger images (@sec-ai-deep-learning-convolutional-layers), but the image statistics (mean subtraction, @def-centring-scaling) must match those used in pretraining.
4. Linear probe accuracy is the standard way to compare learnt representations: a better backbone gives a better linear classifier on fixed codes.

:::
