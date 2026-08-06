<p align="center">
  <img src="assets/logo2_pintree.png" alt="SiPE logo" width="140"/>
</p>

<h1 align="center">Beyond Sequence Order:<br>Syntax-Informed Positional Embeddings for Transformers</h1>

<p align="center">
  <a href="https://hriaz17.github.io/SiPE/"><img src="https://img.shields.io/badge/🌐_Blog-SiPE-B45F06" alt="Blog"></a>
  <a href="#citation"><img src="https://img.shields.io/badge/📖_Paper-Under_Review-2E7D32" alt="Paper"></a>
  <img src="https://img.shields.io/badge/Code-Coming_Soon-lightgrey" alt="Code coming soon">
</p>

<p align="center">
  <a href="https://hriaz17.github.io/">Haris Riaz</a> ·
  Hyungji Kim ·
  <a href="https://surdeanu.cs.arizona.edu/mihai/">Mihai Surdeanu</a>
  <br>
  <em>Department of Computer Science, University of Arizona</em>
</p>

---

**SiPE** (**S**yntax-**i**nformed **P**ositional **E**mbeddings) learns a lightweight syntactic prior from dependency parses during pretraining and injects it into the *positional pathway* of Transformers — across all three dominant positional-encoding families (absolute, relative, rotary), for both encoders and decoders. Conditioning on a **single parse** at inference, SiPE improves SyntaxGym by up to **10.3%** while *simultaneously reducing* perplexity by **9.0%**, and lifts GLUE scores by up to **8.2%** — establishing a new Pareto frontier between syntactic supervision and inference cost.

<p align="center">
  <img src="docs/assets/teaser.png" alt="SiPE Pareto frontier" width="55%"/>
</p>

## Code

> 🚧 **Code, hexatagged training data, and pretrained checkpoints will be released upon acceptance.**

## Citation

```bibtex
@misc{riaz2026sipe,
  title  = {Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers},
  author = {Riaz, Haris and Kim, Hyungji and Surdeanu, Mihai},
  year   = {2026},
  note   = {Under review}
}
```
