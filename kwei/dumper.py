from pathlib import Path

from datasets import Dataset, load_dataset, tqdm


def dump(name: str, split: str, lang1: str, lang2: str):
    path1 = Path('data') / name / f'{lang1}-{lang2}' / f'{split}.{lang1}'
    path2 = Path('data') / name / f'{lang1}-{lang2}' / f'{split}.{lang2}'
    path1.parent.mkdir(exist_ok=True, parents=True)

    with path1.open(mode='w', encoding='utf-8') as fp1:
        with path2.open(mode='w', encoding='utf-8') as fp2:
            for data in tqdm(load_dataset(name, f'{lang1}-{lang2}', split=split)):
                print(data['translation'][lang1].strip(), file=fp1)
                print(data['translation'][lang2].strip(), file=fp2)


def load(path1: Path, path2: Path, lang1: str, lang2: str) -> Dataset:
    ds = []

    with path1.open(mode='r', encoding='utf-8') as fp1:
        with path2.open(mode='r', encoding='utf-8') as fp2:
            for text1, text2 in zip(fp1, fp2):
                text1 = [int(idx) for idx in text1.strip().split()]
                text2 = [int(idx) for idx in text2.strip().split()]

                ds.append({
                    'text1': text1, 'lang1': lang1, 'size1': len(text1),
                    'text2': text2, 'lang2': lang2, 'size2': len(text2),
                })

    ds = Dataset.from_list(ds)
    print(f'ds => {ds}')
    return ds
