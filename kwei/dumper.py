from pathlib import Path

from datasets import load_dataset, tqdm


def dump(name: str, sub: str, split: str, lang1: str, lang2: str):
    path1 = Path('out') / name / sub / f'{split}.{lang1}'
    path2 = Path('out') / name / sub / f'{split}.{lang2}'
    path1.parent.mkdir(exist_ok=True, parents=True)

    with path1.open(mode='w', encoding='utf-8') as fp1:
        with path2.open(mode='w', encoding='utf-8') as fp2:
            for data in tqdm(load_dataset(name, sub, split=split)):
                print(data['translation'][lang1].strip(), file=fp1)
                print(data['translation'][lang2].strip(), file=fp2)
