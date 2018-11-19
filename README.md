# finder
Finder will search google for pages then scrape them for email address



## Two files loooku

The finder will use the two textfiles to add as search in the following setup


If the file first.txt has the contet of 

```
hej
bu
bo
```


And the secound.txt has the contnet of


```
fu
se
de
```


We will do google search for


hej fu
hej se
hej de


bu fu
bu se
bu de


bo fu
bo se
bo de


## Mailchimp


Add to the assmailchimp your api key and the id of the lits that you wnat the email to be store


### csv

Defult all email will be saved to the files email.csv



## To run


```

docker-compose up

```


# fins-worker
