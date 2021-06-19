# GRX (Gist Request X)

This is a program that sends requests to the Gist API and receives the response. For every Gist from the Gists response, it sends a request to those Gist's File RAW URL (if there are more than 1 file, then it scours all of the RAW URLs) and gives a response. The monitor folder then checks all of the files and lets the user know if anything is found. 

## How To Run
Install all of the required packages/modules in `requirements.txt` with Pip3, then run the `main.py` file.

```bash
$ python3 src/main.py 
```
*Inspired by https://github.com/tillson/git-hound/*