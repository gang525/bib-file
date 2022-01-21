# MDO Lab Reference Bibliography

This is the reference BibTeX bibliographic database for the MDO Lab. Please observe the following guidelines:

* I do not provide write access to this file (in part because the software I use to handle the bib file (BibDesk) is picky and changes that would normally work might break it, and there are other reasons).

* This file is a clean version of the bib file I keep in BibDesk. I use bibtool to remove BibDesk custom fields and notes.

* If you have corrections to mdolab.bib, message or email them to me <jrram@umich.edu>. If you have a lot of changes, please make clear which entries are new and which entries are edits to existing ones. Please make sure that you do not send me duplicates.

* Please update as soon as you publish a new paper.

* Make sure you do not add entries that are already in there.

* Please use this file as your starting point. Do not create bib entries from scratch if they are in this file, and please follow the conventions in this file when you create new entries. Unless you have a very good reason, please use the same convention for the keys (first author last name + year + unique character `a`,`b`,...)

* Do not be lazy and rely on bibtex entries directly downloaded from the web, or automatically generated entries. Make it consistent with current mdolab.bib (although not all are currently consistent; work in progress!).

* Do not use the "URL" field, only the "doi" one, which will already be hyperlinked to the source.

* Do not use `{}` to protect the case for whole entries (like the title). (Reason: Wether the title gets capitalizes all the words in the title or not, is up to the bibtex style bst file.)

* On the other hand, do protect the capitalization of acronyms and proper names in the title, e.g. `{RANS}`, `{N}ewton`.

* For the month, spell the month in full, e.g., `November`.

* When using this file, create a soft link to it in the paper directory (I have an alias defined in my `.bash_profile` for this: `alias lnsbib='ln -s ~/_jrram/bib-file/mdolab.bib mdolab-link.bib`). This soft link should not be tracked in a repo.

* When the paper is finalized and submitted, remove the mdolab.bib soft link, copy the actual file and add it to the paper repo, but using a *different name*, e.g., mdolab-copy.bib. This will ensure that the document can be recompiled with not reference issues in the future.

* As soon as you submit your final paper to a conference or your journal paper is accepted, please send the BibTeX entry to me. It is your responsibility to make sure that all the papers you co-author are correctly and completely represented in mdolab.bib.
