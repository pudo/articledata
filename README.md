# articledata 

A Python-based metadata specification for exchanging news articles between different systems. The purpose of this is to differentiate between a media crawling/extraction and mining/NLP phase of a media analytics system. 

`articledata` files are line-delimited JSON files with each row describing an object with the structure detailed in [article.py](https://github.com/pudo/articledata/blob/main/articledata/article.py). It's a convention to use SHA1 hashes of each article's normalized URL as the `id` for the article. Of course, if unique identifiers from the sources CMS are available, they might be used instead, ideally with a unique prefix: `spiegel-187281`.

`articledata` is purely a specification package, it does not contain any article processing code (e.g. crawling, NLP).

## Installation

`articledata` is on `pypi`:

```bash
pip install articledata
```

## Uses of articledata

`articledata` is used to move crawled news articles between these applications:

* [`storyweb`](https://storyweb.opensanctions.org/) - an app to extract actor networks from corpora of news reporting.
* [`mediacrawl`](https://github.com/opensanctions/mediacrawl) - a tool for crawling articles from a particular set of domains and extracting the article body.

## License

See `LICENSE`, it's an MIT-style scheme.