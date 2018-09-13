
# Create a hand-crafted list of tokens from existing promo codes

  $ cat tokens.txt
  FORTY
  FIFTY
  SIXTY
  SEVENTY
  EIGHTY
  NINETY
  30
  40
  50
  60
  70
  80
  90
  %
  £
  1
  BUY
  OFF
  ON
  SEP
  PIZ
  LOVE

# Generate the dictionary of passwords from the tokens

  $ python tokens2code.py

# Run the scraping script

  $ while true; do date; python test_codes.py ; sleep 1; done
