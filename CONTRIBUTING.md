# How to contribute 

## Did you find a bug?

Submit it in the [issue tracker](https://github.com/martisak/3gpp-citations/issues).

## Do you have questions about the source code?

Send us your question in [Gitter IM](https://gitter.im/3gpp-citations/community).

## Submitting changes

Please send a GitHub Pull Request to 3gpp-citations with a clear list of what you've done ([read more](https://help.github.com/articles/about-pull-requests/) about pull requests). When you send a pull request, we will love you forever if you include a minimum working example (MWE) when applicable. We can always use more test coverage. Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this

~~~~
$ git commit -m "Category: A brief summary of the commit
> 
> A paragraph describing what changed and its impact."
~~~~

where Category is in [`Enhancement`, `Documentation`, `Fix`, `Refactor`].

### Do you want to contribute to the documentation?

Submit a pull request. Tag your commits with `Documentation`.

### Did you write a patch that fixes a bug?

Submit a pull request. Tag your commits with `Fix`. 

### Did you refactor the code?

Submit a pull request. Tag your commits with `Refactor: [method]` where `method` can be one of [these](https://refactoring.guru/refactoring/techniques) or free text.

### Did you fix whitespace, format code, or make a purely cosmetic patch?

Submit a pull request. Tag your commits with `Refactor: cosmetic - ` and some explaining text. 

### Do you intend to add a new feature or change an existing one?

Submit a pull request. Tag your commits with `Enhancement`.

## Coding conventions

- We follow [PEP8](https://www.python.org/dev/peps/pep-0008/) to the letter.
