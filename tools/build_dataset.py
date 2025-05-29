import argparse
import json
import os
import re
from typing import List

CODE_BLOCK_RE = re.compile(r"```(?:pine|pinescript|pine-script)?\n(.*?)```", re.DOTALL | re.IGNORECASE)


def extract_from_markdown(text: str) -> List[str]:
    """Return pine script code blocks from markdown text."""
    return [block.strip() for block in CODE_BLOCK_RE.findall(text)]


def collect_examples(input_dir: str) -> List[dict]:
    """Walk through input_dir and collect pine script examples."""
    examples = []
    for root, _, files in os.walk(input_dir):
        for name in files:
            path = os.path.join(root, name)
            if name.lower().endswith(".md"):
                with open(path, "r", encoding="utf-8") as fh:
                    text = fh.read()
                for block in extract_from_markdown(text):
                    examples.append({"code": block, "source": os.path.relpath(path, input_dir)})
    return examples


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect Pine Script examples from docs")
    parser.add_argument("input_dir", help="Path to downloaded TradingView documentation")
    parser.add_argument("output", help="Path to output JSONL dataset")
    args = parser.parse_args()

    examples = collect_examples(args.input_dir)
    with open(args.output, "w", encoding="utf-8") as out:
        for ex in examples:
            out.write(json.dumps(ex, ensure_ascii=False) + "\n")

    print(f"Wrote {len(examples)} examples to {args.output}")


if __name__ == "__main__":
    main()
