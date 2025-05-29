# pinealgos

Utilities for working with Pine Script.

## Building the dataset

Download the TradingView documentation to a local directory. The files should be Markdown so that Pine Script examples are enclosed in fenced code blocks.

Run the dataset builder with the path to the docs directory and an output file:

```bash
python tools/build_dataset.py path/to/docs dataset.jsonl
```

The resulting `dataset.jsonl` will contain one JSON object per line with the following fields:

- `code`: the extracted Pine Script snippet
- `source`: relative path to the documentation file where the snippet came from

Use this dataset as input for model training pipelines.


## Pine Script development

Use this repository to experiment with Pine Script examples. When adding new scripts:

- Refer to the official [TradingView documentation](https://www.tradingview.com/pine-script-docs/) for language details.
- Put each example in its own file or folder with a clear, descriptive name.
- Comment your code with links or references to the relevant documentation sections.
- Keep examples short and educational, and include a small README explaining what each script demonstrates.

