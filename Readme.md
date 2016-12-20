# Heritrix crawllog analysis
[![Build Status](https://travis-ci.org/dbmdz/heritrix-harvest-analysis.svg?branch=master)](https://travis-ci.org/dbmdz/heritrix-harvest-analysis)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ba2014ecbe0c4c01b89968385a3ff377)](https://www.codacy.com/app/marcus_2/heritrix-harvest-analysis?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dbmdz/heritrix-harvest-analysis&amp;utm_campaign=Badge_Grade)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

## Introduction

Large harvests are a hard task for QA without proper tools. These scripts will help you with semi-manual quality assurance by grouping and filtering data and calculating metrics.

## System Requirements

Standard Python 3.x without any extra packages.

## Commands

### Duplicate Checking

Checks a crawl.log for duplicate files determined by hash value. This is useful if your harvest is unexpectedly big as a website might deliver the same content under different URLs (there are for example websites delivering wrong pages instead of 404 response codes).

You can filter for URLs corresponding to certain response codes. If you don't, everything is analyzed.

Usage:

    $ python check_for_duplicates.py --help
    usage: check_for_duplicates.py [-h] [-o OUT] [-c CODE] crawl_log

    positional arguments:
     crawl_log

    optional arguments:
     -h, --help            show this help message and exit
     -o OUT, --out OUT
     -c CODE, --code CODE  HTTP response code to filter before checking for
                           duplicates.
Examples:

    $ python check_for_duplicates.py -o report.txt crawl.log
    $ python check_for_duplicates.py -o report.txt -c 404 crawl.log

### Compare Logfiles

You ran two crawls with different settings and want to know how the crawl has changed? `look_for_missing_urls.py` compares two `crawl.log` files and generates a report which URLs are missing in the *second* one

Usage:

    $ python look_for_missing_urls.py --help
    usage: look_for_missing_urls.py [-h] [-o OUT] reference compare

    positional arguments:
     reference
     compare

    optional arguments:
     -h, --help         show this help message and exit
     -o OUT, --out OUT

Example:

    $ python look_for_missing_urls.py -o difference.txt reference.log other.log

### Sort by Response Code

The script `sort_by_response_code.py` sorts all URLs by response code.

Usage:

    $ python sort_by_response_code.py --help
    usage: sort_by_response_code.py [-h] [-o OUT] crawl_log

    positional arguments:
      crawl_log

    optional arguments:
      -h, --help         show this help message and exit
      -o OUT, --out OUT

Example:

    $ python sort_by_response_code.py -o sorted.txt crawl.log


### Count URLs per domain

This analyzer uses already the new unified API and count the number of URLs per domain.

Usage:

    $ python crawllog.py urls-per-domain --help
    usage: crawllog.py domains [-h] [--code CODE] [--out OUT] logfile

    positional arguments:
    logfile      The crawl.log to process.

    optional arguments:
    -h, --help   show this help message and exit
    --code CODE  Only count URLs for given response code.
    --out OUT    Only count URLs for given response code.

Examples:

  - count downloaded URLs per domain (that is, URLs with response code 200):

        $ python crawllog.py urls-per-domain --code 200 crawl.log

  - count all URLs for all domains the harvester visited (meaning any response code):

        $ python crawllog.py urls-per-domain crawl.log