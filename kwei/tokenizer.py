import subprocess

from kwei import moses_tokenizer_dir


def moses_tokenize(text: str, lang: str = 'en') -> str:
    text = text.replace('"', '\\\"')
    out = subprocess.run(
        f'echo "{text}" |'
        f'perl {moses_tokenizer_dir}/replace-unicode-punctuation.perl | '
        f'perl {moses_tokenizer_dir}/normalize-punctuation.perl | '
        f'perl {moses_tokenizer_dir}/remove-non-printing-char.perl | '
        f'perl {moses_tokenizer_dir}/tokenizer.perl -q -l {lang} -a -b -no-escape',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, shell=True,
    )

    if out.returncode == 0:
        return out.stdout.strip()

    raise RuntimeError(out.stderr)


def moses_detokenize(text: str, lang: str = 'en') -> str:
    text = text.replace('"', '\\\"')
    out = subprocess.run(
        f'echo "{text}" | perl {moses_tokenizer_dir}/detokenizer.perl -q -l {lang} -b',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, shell=True,
    )

    if out.returncode == 0:
        return out.stdout.strip()

    raise RuntimeError(out.stderr)
