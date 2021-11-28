import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'poocoin_trending'

setuptools.setup(
    name='poocoin_trending',
    version='0.0.2',
    author='Kristóf-Attila Kovács',
    description='poocoin_trending',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/py_poocoin_trending',
    packages=setuptools.find_packages(),
    install_requires=[
        'jsoncodable>=0.1.7',
        'kcu>=0.0.73',
        'ksimpleapi>=0.0.41'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)