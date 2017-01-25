# semantic-pdf-splitter

Playground for using [luigi](https://github.com/spotify/luigi/), [PyPDF2](https://github.com/mstamy2/PyPDF2) and [nltk](http://www.nltk.org/).

Reads PDF Files from a given folder an splits it according to the cosine similarity of the extracted texts. Work load is balanced and can be monitored by luigi.

Each file will be processed only once, as luigi detects which work is done.

## Installation
```
git clone .

pip install nltk
pip install luigi
pip install pypdf2

touch stopwords.txt ### Add desired stop words to this text file, divided by newline
```

## Usage
```
luigid &

PYTHONPATH='.' luigi --workers 4 --module semantic_pdf_splitter GetFiles --fin /home/user/Documents/PDF/ --fout ./target/
```

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

## History

## Credits
- Martin Franke (MtnFranke)

## License
MIT License
