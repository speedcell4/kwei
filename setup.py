from pathlib import Path

from setuptools import setup

name = 'kwei'

root_dir = Path(__file__).parent.resolve()
with (root_dir / 'requirements.txt').open(mode='r', encoding='utf-8') as fp:
    install_requires = [install_require.strip() for install_require in fp]

setup(
    name=name,
    version='0.1.0',
    packages=[name],
    include_package_data=True,
    package_data={
        name: ['moses/**/*'],
    },
    url=f'https://github.com/speedcell4/{name}',
    license='MIT',
    author='speedcell4',
    author_email='speedcell4@gmail.com',
    python_requires='>=3.8',
    install_requires=install_requires,
)
