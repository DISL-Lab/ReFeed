<h1 align="center">
♻️ ReFeed (COLM'25)
</h1>


<h3 align="center">
ReFeed: Multi-dimensional Summarization Refinement with Reflective Reasoning on Feedback
</h3>



<div align="center">
  <p>Authors: Taewon Yun, Jihwan Oh, Hyangsuk Min, Yuho Lee, Jihwan Bang, Jason Cai, Hwanjun Song</p>
  <a href="https://arxiv.org/abs/2503.21332">
  <img src="https://img.shields.io/badge/arXiv-b31b1b?style=flat-square" alt="arXiv">
  </a>
  <a href="https://disl-lab.github.io/">
  <img src = "https://img.shields.io/badge/Data%20Intelligence%20System%20Lab-B552CB.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iNTQ0LjAwMDAwMHB0IiBoZWlnaHQ9IjU0MS4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDU0NC4wMDAwMDAgNTQxLjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsNTQxLjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTExNDggNDQzOSBsLTMgLTk1MSAtNzMgLTE5IGMtNTQwIC0xMzcgLTk1NSAtNTk0IC0xMDM2IC0xMTQxIC0xMTEKLTc0NyAzODUgLTE0NDQgMTEyOSAtMTU4NCA2NyAtMTIgMTY4IC0xOCAzOTMgLTIxIGwzMDIgLTUgMCAtMzU1IDAgLTM1NSA1NjgKNSBjNDQ1IDMgNTkwIDggNjcyIDIwIDQ4NyA3MiA5MjYgMjYxIDEzMDAgNTU3IDEyNCA5OCAzMzggMzEwIDQzNCA0MzAgMjc3CjM0NyA0NzggNzk2IDU1MCAxMjMwIDQxIDI0NSA0NiA1OTUgMTEgODI4IC02OSA0NzQgLTI2OCA5MzUgLTU2MSAxMzAyIC04NwoxMDkgLTMxNSAzMzcgLTQyNCA0MjQgLTMxNSAyNTEgLTY5MSA0MzEgLTEwOTEgNTIyIC0yNTUgNTcgLTI0OSA1NyAtMTI0NiA2MQpsLTkyMyA0IC0yIC05NTJ6IG0xOTQyIDU5NyBjNDEzIC02OSA3OTYgLTIzNyAxMTA1IC00ODQgODIzIC02NjAgMTExNCAtMTc1Nwo3MjYgLTI3MzUgLTE3MCAtNDI3IC00OTcgLTgyNSAtODk2IC0xMDkxIC0zMDUgLTIwNCAtNjg4IC0zMzkgLTEwNTkgLTM3NSAtNjAKLTYgLTI1OSAtMTEgLTQ0MyAtMTEgbC0zMzMgMCAwIDE5MCAwIDE5MCAyOTggMCBjNDQwIDAgNjE4IDIyIDg3MCAxMDYgMjg0IDk1CjUyMyAyNDAgNzQ1IDQ1MyAyNjAgMjUwIDQzNSA1NDYgNTM3IDkwOSA4NiAzMDQgODcgNjg4IDQgMTAwOCAtMjIzIDg1OSAtMTAwMgoxNDcxIC0xODc5IDE0NzcgLTk4IDAgLTE2MiAtNSAtMjE0IC0xNiAtMzE5IC03MyAtNTYzIC0zMDAgLTY1NyAtNjE0IC0yNSAtODEKLTI3IC0xMDYgLTMyIC0zMDUgbC00IC0yMTggLTEzNyAwIGMtNzUgMCAtMTYwIC0zIC0xODggLTYgbC01MyAtNyAwIDc3NyAwCjc3NyA3NTMgLTQgYzY2MCAtMyA3NjUgLTUgODU3IC0yMXogbS0xNzAgLTcwMSBjOTQ1IC0xMTAgMTU5NiAtOTg0IDE0MzQKLTE5MjUgLTE5IC0xMTQgLTc5IC0yOTkgLTEzMiAtNDEyIC0yMTAgLTQ0OCAtNjE2IC03NzkgLTExMDcgLTkwMiAtMTM3IC0zNQotMjkwIC00NiAtNjExIC00NiBsLTMxNCAwIDAgMTk1IDAgMTk1IDMyOSAwIGMzOTkgLTEgNDc2IDkgNjc4IDg2IDIyNSA4NiA0NDcKMjY2IDU4OCA0NzggMjE1IDMyNCAyNjcgNzQwIDEzOCAxMTEwIC00MiAxMjEgLTY5IDE3NSAtMTQxIDI4NiAtNjggMTA0IC0yNDAKMjc4IC0zMzcgMzQyIC0yMTIgMTM5IC00NTkgMjE4IC02ODAgMjE4IC02OSAwIC04NyAtNCAtMTE1IC0yMiAtNzggLTUzIC0xMDAKLTEzOCAtNTggLTIxNyAzNCAtNjMgNzUgLTgxIDIwMyAtOTEgMzY0IC0zMCA2NTYgLTI0MCA4MDAgLTU3NyA0NyAtMTEwIDY4Ci0yMTcgNjkgLTM1MyAxIC0zNjIgLTIwMCAtNjgyIC01MjggLTg0MCAtMTc2IC04NCAtMjY4IC05OCAtNjczIC05OSBsLTI3MyAtMgowIDEwNTkgYzAgOTA1IDIgMTA2NiAxNSAxMTE1IDUxIDE5OCAyMTggMzU5IDQxNSA0MDEgODYgMTkgMTQ5IDE5IDMwMCAxegptLTEwNjIgLTE4NTcgbC0zIC03MTMgLTU3IDMgYy0xMzMgNiAtMjUzIDg5IC0yOTYgMjA1IC0yMiA1NyAtMjIgNjggLTIyIDYzNwpsMCA1ODAgMTkwIDAgMTkwIDAgLTIgLTcxMnogbS03MDggMTA1IGMwIC02MzggMCAtNjM2IDcyIC03ODMgMzMgLTY3IDYwIC0xMDIKMTIzIC0xNjUgMTIzIC0xMjQgMjQ5IC0xODEgNDIwIC0xOTQgbDkwIC02IDMgLTE5MyAyIC0xOTQgLTMwMiA1IGMtMjI0IDQKLTMyMCA5IC0zNjggMjAgLTQyOSAxMDIgLTc1MiA0MzYgLTgyNSA4NTQgLTE5IDEwOCAtMTkgMjc0IC0xIDM3OCA2NyAzNzggMzQzCjY5OCA3MTEgODI0IDMzIDExIDYzIDIwIDY4IDIxIDQgMCA3IC0yNTUgNyAtNTY3eiIvPgo8L2c+Cjwvc3ZnPgo=&style=flat-square">
  </a>

  <img src = "https://img.shields.io/badge/KAIST%20GSDS-087CFA.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMzk3LjAwMDAwMHB0IiBoZWlnaHQ9IjEyNC4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDM5Ny4wMDAwMDAgMTI0LjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsMTI0LjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTM3NyAxMTA1IGMtMTE2IC0zMiAtMjAyIC0xMzEgLTIyNiAtMjYwIC0xNCAtNzQgLTE0IC0yNjAgLTEgLTM0NAoyMCAtMTE3IDg2IC0yMDggMTg0IC0yNTIgMTIwIC01MiA0NjcgLTUwIDU2MCA1IDkwIDUzIDExNiAxMjEgMTE2IDMwOCBsMCAxMjgKLTE4NSAwIC0xODUgMCAwIC05MCAwIC05MCA4NiAwIDg3IDAgLTYgLTQyIGMtOSAtNjQgLTE5IC02OCAtMTk3IC02OCAtMTQ2IDAKLTE1OSAyIC0xOTAgMjMgLTY2IDQ0IC03NSA3MyAtNzUgMjQ3IDAgMTcxIDggMTk5IDY4IDI0NCAyNyAyMCA0MiAyMSAyNzggMjQKbDI0OSAzIDAgODkgMCA5MCAtMjU3IC0xIGMtMTgxIC0xIC0yNzIgLTUgLTMwNiAtMTR6Ii8+CjxwYXRoIGQ9Ik0yMDYwIDY3MCBsMCAtNDUwIDI2OCAwIGMzNDEgMCAzOTEgMTIgNDc3IDExMiA2NyA3OSA3OSAxMjkgNzkgMzM4CjAgMjA5IC0xMiAyNTkgLTc5IDMzOCAtODYgMTAwIC0xMzYgMTEyIC00NzcgMTEyIGwtMjY4IDAgMCAtNDUweiBtNTYxIDI0NwpjNjAgLTQwIDY5IC03MiA2OSAtMjQ3IDAgLTE3NSAtOSAtMjA3IC02OSAtMjQ3IC0zMiAtMjIgLTQ0IC0yMyAtMjAyIC0yMwpsLTE2OSAwIDAgMjcwIDAgMjcwIDE2OSAwIGMxNTggMCAxNzAgLTEgMjAyIC0yM3oiLz4KPHBhdGggZD0iTTEyNzcgMTA5MyBjLTY2IC0yMiAtMTQxIC05MSAtMTY0IC0xNTEgLTQyIC0xMTIgLTMgLTI0NyA5MCAtMzA5IDcwCi00NyAxMDQgLTU0IDI4NSAtNjAgMTQ5IC01IDE2NiAtOCAxODkgLTI3IDM2IC0zMSAzNSAtOTIgLTIgLTEyMyAtMjYgLTIzIC0zMAotMjMgLTI4NiAtMjMgbC0yNTkgMCAwIC05MSAwIC05MCAzMDggMyAzMDcgMyA1NCAzMCBjODggNDkgMTMzIDEyNiAxMzQgMjMxIDEKMTE3IC03NyAyMjEgLTE5MSAyNTQgLTIwIDYgLTExMSAxNCAtMjAyIDE3IC0xNTQgNiAtMTY1IDggLTE4NyAyOSAtMjUgMjYgLTMxCjc4IC0xMCAxMDUgMjcgMzYgNTMgMzkgMjg2IDM5IGwyMzEgMCAwIDkwIDAgOTAgLTI2NyAtMSBjLTIxOSAwIC0yNzcgLTMgLTMxNgotMTZ6Ii8+CjxwYXRoIGQ9Ik0zMTczIDEwOTYgYy0xMzcgLTQzIC0yMTIgLTE3MCAtMTgzIC0zMDkgMTIgLTYwIDUxIC0xMjIgOTcgLTE1NSA1OQotNDIgMTIxIC01NCAyOTEgLTYwIDE5MyAtNiAyMTIgLTEzIDIxMiAtODcgMCAtMzUgLTUgLTQ4IC0yNiAtNjQgLTI1IC0yMCAtMzkKLTIxIC0yOTAgLTIxIGwtMjY0IDAgMCAtOTEgMCAtOTAgMzA4IDMgYzI4OCAzIDMxMCA0IDM1MyAyNCAyNSAxMiA2MCAzNyA3OAo1NSAxMTAgMTE0IDk0IDMxMSAtMzIgMzk2IC02OSA0NiAtMTAyIDUzIC0yODcgNjAgLTE1NCA2IC0xNjUgOCAtMTg3IDI5IC0xNAoxNCAtMjMgMzUgLTIzIDUzIDAgODUgMTkgOTEgMzAwIDkxIGwyMzAgMCAwIDkwIDAgOTAgLTI2NyAtMSBjLTE5MSAwIC0yODAgLTQKLTMxMCAtMTN6Ii8+CjwvZz4KPC9zdmc+Cg==&style=flat-square">
  

<p align="center">
  <img src="./imgs/refeed_overview.png" style="width: 100%;" id="title-icon">
</p>

</div>

> This is the official github repository for "ReFeed: Multi-dimensional Summarization Refinement with Reflective Reasoning on Feedback"

## 📄 Table of Contents
- [📌 Table of Contents](#-table-of-contents)
  - [Overview](#overview)
  - [Datasets](#datasets)
  - [Quick Start](#quick-start)
    - [Training Setup](#training-setup)
    - [Launch Training](#launch-training)
  - [Results](#evaluation)
  - [Citation](#citation)
  - [Acknowledgement](#acknowledgement)

## Overview


ReFeed rethinks summary refinement by showing that reflective reasoning over multi-dimensional feedback is key to achieving balanced, robust improvements. 

Our contributions:

* 🧠 **Introduces reflective reasoning for multi-dimensional refinement**, enabling models to resolve trade-offs, mitigate order bias, and filter noisy feedback simultaneously
* 🏗️ **Releases SumFeed-CoT**, a large-scale Long-CoT dataset that distills high-quality reflective reasoning from large reasoning models into lightweight models
* 🚀 **Demonstrates strong empirical gains and robustness**, achieving consistent improvements across faithfulness, completeness, and conciseness while remaining resilient to feedback quality and ordering

## 🤗 Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| SumFeed-CoT | Training set for ReFeed (7713 samples) | [🤗](https://huggingface.co/datasets/DISLab/SumFeed-CoT) |

## 🛠️ Quick Start

### Training Setup

1. **Environment Setup**
   - Ensure all dependencies are properly installed and configured.

2. **Data Preparation**
   - Obtain the SumFeed-CoT dataset from [🤗 Hugging Face](https://huggingface.co/datasets/DISLab/SumFeed-CoT).

3. **Configuration**
   - Use our provided [configuration file](./configs/zero3.yaml).

### Launch Training

For training, use the following command:

```bash
sh ./script/sft.sh
```

## 📄 Results


<p align="center">
  <img src="./imgs/refeed_results.png" style="width: 85%;" id="title-icon">
</p>

* 📈 **ReFeed achieves the best overall performance** across faithfulness, completeness, and conciseness, outperforming all previous refinement methods that optimize a single dimension.
* ⚖️ **Reflective reasoning enables balanced improvements**, effectively mitigating trade-offs that arise when optimizing multiple dimensions simultaneously.
* 🔀 **Strong robustness to feedback order and noise**, showing minimal performance variance under shuffled or low-quality feedback settings.
* 🧩 **Efficient distillation**: a lightweight 8B model matches teacher-level refinement quality while significantly reducing inference cost.

## 🖇️ Citation

Please consider citation if our paper is useful in your research.
```BibTeX
@inproceedings{yun2025refeed,
    title={ReFeed: Multi-dimensional Summarization Refinement with Reflective Reasoning on Feedback},
    author={Taewon Yun and Jihwan Oh and Hyangsuk Min and Yuho Lee and Jihwan Bang and Jason Cai and Hwanjun Song},
    booktitle={Second Conference on Language Modeling},
    year={2025},
    url={https://openreview.net/forum?id=6BGDGKZN7q}
}
```

## 🙏 Acknowledgement
This research was supported by KISTI, and by the NRF. For GPU infrastructure, our work was supported by the IITP grant funded by MSIT.

###### *This work was done @ KAIST Data Intelligence System Lab*