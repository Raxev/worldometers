<h1 align="center">World-o-Meters</h1>
<p align="center">Web Scraping with Python using the Scrapy Framework</p>

## What is this project for?

This is a project where I apply what I've learned about Web Scraping.

## Table of contents

- [Quick Start](#quick-start)
- [Local Deploy Steps](#local-deploy-steps)
- [Run the Spider of your choice](#run-the-spider-of-your-choice)
- [Export output as CSV, Json, or XML](#export-output-as-csv-json-or-xml)
- [Notes](#notes)
- [To do](#to-do)

## Quick start


- Clone the repo: `git clone https://github.com/Raxev/worldometers.git`


## Local Deploy steps

Install the required dependencies:

    $ pip install -r requirements.txt

## Run the Spider of your choice

    scrapy crawl countries
    scrapy crawl gdp_debt

## Export output as CSV, Json, or XML

    scrapy crawl <spider.name> -o <filename.extension>

## Notes

## To do
