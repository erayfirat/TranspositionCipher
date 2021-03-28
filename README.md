# Transposition Cipher

I implemented a very old and basic cryptography algorithm. 
This algorithm was used by the German military in World War 1. 
The system was regularly solved by the French, naming it Ubchi, who were typically able to find the key in a matter of days after a new one had been introduced. 
However, the French success became widely known and,after a publication in Le Matin, the Germans changed to a new system on 18 November 1914.
DuringWorldWar II, an advanced version of this cipher was used by Dutch Resistance groups, the French Maquis and the British Special Operations Executive (SOE). 
It was also used as an emergency cipher for the German Army and Navy. Until the discovery of the VIC cipher, this was generally regarded as the most complicated cipher that an agent could operate reliably under difficult field conditions.

"encryption" method take a String message and a key (also a String) and mix the order of letters. 
The messageis written out in rows of a fixed length, and then read out again column by column, and the columns are chosen in some scrambled order. 
Both the length of the rows and the permutation of the columns are usually defined by a keyword.
I use dictionary to encrypt text.

"decryption" method opposite of encryption method. I takes encrypted text to plain text.
I use matrice to get plain text. 
