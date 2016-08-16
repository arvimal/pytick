## README - Pytick 

`pytick` is intended to be an easy-to-use tool/tracker for answering tickets in support organisations. 

The idea is to keeps track of various stats and information related to the cases worked on. 

Some of the features (or upcoming ones) are :

1. Open new cases.
2. Open existing cases.
3. Search for keywords and list relevant cases.
4. Add relevant info to the cases such as:
	1. Knowledge base articles
	2. Worked hours
	3. Shift timings, if applicable.
5. Print reports of cases worked on various search criteria.
6. ..Several others..


### Features in alpha v1:

1. Open new cases
2. Open existing cases.
3. `pytick` will create the necessary dir heirarchy to store the data, if run for the first time.
4. On subsequent runs, it will show the user the `pytick >>>` prompt.

### Fixes 

1. If a ticket number is not mentioned with 'open', pytick will prompt for an input.
2. Initially only a single ticket can be opened with 'open' and the editor needs to be closed to get to another one. This has been rectified by passing the control back to `pytick`. With this fix, multiple cases can be opened one by one.
3. 'open' only accepts integers.
4. Prints proper help if expected arguments are not passed for each keyword.
