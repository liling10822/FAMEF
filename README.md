https://doi.org/10.6084/m9.figshare.13218755.v1
# README-analysis
## Install from GitHub
To run SOMEF, please follow the next steps:

Clone this GitHub repository

```
git clone https://github.com/liling10822/SOMEF_Extension-.git
```

Install somef (note that you should be in the folder that you just cloned)

```
cd somef
pip install -e .
```

Test SOMEF installation

```bash
somef --help
```

If everything goes fine, you should see:

```bash
Usage: somef [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  configure  Configure credentials
  describe   Running the Command Line Interface
  version    Show somef version.
```


## Usage 

### Configure
Before running SOMEF, you must configure it appropriately. Run

```bash
somef configure
```

And you will be asked to provide the following: 

- A GitHub authentication token [**optional, leave blank if not used**], which SOMEF uses to retrieve metadata from GitHub. If you don't include an authentication token, you can still use SOMEF. However, you may be limited to a series of requests per hour. For more information, see [https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) 
- The path to the trained classifiers (pickle files). If you have your own classifiers, you can provide them here. Otherwise, you can leave it blank

### Run SOMEF

```bash
$ somef describe --help
  SOMEF Command Line Interface
Usage: somef describe [OPTIONS]

  Running the Command Line Interface

Options:
  -t, --threshold FLOAT           Threshold to classify the text  [required]
  Input: [mutually_exclusive, required]
    -r, --repo_url URL            Github Repository URL
    -d, --doc_src PATH            Path to the README file source
    -i, --in_file PATH            A file of newline separated links to GitHub
                                  repositories

  Output: [required_any]
    -o, --output PATH             Path to the output file. If supplied, the
                                  output will be in JSON

    -g, --graph_out PATH          Path to the output Knowledge Graph file. If
                                  supplied, the output will be a Knowledge
                                  Graph, in the format given in the --format
                                  option

  -f, --graph_format [turtle|json-ld]
                                  If the --graph_out option is given, this is
                                  the format that the graph will be stored in

  -h, --help                      Show this message and exit.
```

## Usage example:
The following command extracts all metadata available from [https://github.com/dgarijo/Widoco/](https://github.com/dgarijo/Widoco/). 

```bash
somef describe -r https://github.com/dgarijo/Widoco/ -o test.json -t 0.8
```
