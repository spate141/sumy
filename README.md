# Automatic text summarizer

------

## ⚠️ :: Fork notes :: ⚠️ 
- **Please refer to original** [**miso-belica/sumy**](https://github.com/miso-belica/sumy) **repo for full functionality of this package.**
- This fork only supports `english` language.
- `Tokenizer` and `PlaintextParser` are updated to generate sentences using `spaCy/en_web_core_sm`.
- There could be many bugs as I've not fully tested other parts of this codebase except changing how the sentences are being generated. 

## Installation
- pip install git+git://github.com/spate141/sumy.git

## Example
```python
import en_core_web_sm
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

LANGUAGE = "english"
SENTENCES_COUNT = 10

text = """New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney's Office by Immigration and Customs Enforcement and the Department of Homeland Security's
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18."""

stemmer = Stemmer(LANGUAGE)
summarizer = LsaSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

nlp = en_core_web_sm.load()
parser = PlaintextParser.from_string(text, Tokenizer(nlp=nlp, min_sen_len=3), nlp)

summary_sentences = []
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    sentence_text = sentence._text.strip(' ')
    summary_sentences.append(sentence_text)

print(summary_sentences)
```
```python
['(CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.\n',
 'A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.\n',
 'Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.\n',
 'On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.\n',
 'After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective\nAnnette Markowski, a police spokeswoman.',
 'In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.\n',
 'Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.\n',
 "The case was referred to the Bronx District Attorney's Office by Immigration and Customs Enforcement and the Department of Homeland Security's\nInvestigation Division.",
 'Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.\n',
 'Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.\n']
```
