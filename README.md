# Ticker Data-Scrapping
A way to get data off of Yahoo Finance for ticks. Currently including whatever is publically traded on major US stock exchanges (currently 8886 stocks including ETFs). *However, some these ticks mayb not be suppoerted.*

The program currently saves your data into a `.json` for you to analyze in any program you desire. I plan on updating this part to allow you to choose your preference of file type saved to as well as the location.

This is bear minimum right now, using `threading`  with `max-workers=8`. Below is a section for [future additions](#future-additions) that'll explain currently proposed changes to the code.

[Contributions are welcome.](#contributions) **Currently, there is no layout for contributions.**

## Benchamrks
Decision to use `threading` is based off of [previous benchmarks](https://edmundmartin.com/beautiful-soup-vs-lxml-speed/), we want this program to scale with performance. Yet, I have added support for `synchronous`. *`AsyncIO` currently doesn't not work*

## Future Additions
Current list of future additions:
* Fix AsyncIO
* Add more customization
  * Allow user to pick amount of workers they want available
  * Which categories they want for the ticks
  * Allow user to pick if they want to get data for all or certain ticks
  * Allow user to pick file type the data is saved to
* Speed up program by transitioning from BS4
* Integrate with other APIs
* Create a contribution template
* Turn into a pip-package
* Add requirements.txt
* Comment code
* MAYBE add GUI??

If you have any additions you'd like to see, let me know. Contributions is encouraged!

## Contributions
Currently do not have a template for posting contributions..
