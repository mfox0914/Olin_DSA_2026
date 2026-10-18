# Smith-Waterman Genome Alignment

## Input and scoring

- `testAgainst` length: 368 bases
- `targetGenome` length: 6387 bases
- Alignment coordinates are 1-based and inclusive.
- Match score: +3
- Mismatch score: -3
- Linear gap penalty: 2

## Alignment results

- Alignment score: 482
- `testAgainst` coordinates: 1-368
- `targetGenome` coordinates: 399-766
- Alignment length: 396 columns
- Matching bases: 269
- Gaps: 56
- Percent identity: 67.93%

```text
Query  TGGCCACCA-CGATAGCAGAATTTTTTCGCGATAATGGAAAGCGAGTCGT-CTTGCTTGC
       ||||.||.| || ||||.||||.|||||||||..|.|||||.||.||||| ||| .||..
Target TGGCGACAACCG-TAGCGGAATATTTTCGCGACCAGGGAAAACGGGTCGTGCTT-TTTAT

Query  CGACT-CACTGACGCGTTATGC-CAGGGC--CGCACGGGAAATCGCTCTGGCCGCCGGAG
       |||.| || ||||.|||||||| | |.||  .|  ||.||..|.||.|||| ||.||| |
Target CGATTCCA-TGACCCGTTATGCGC-GTGCTTTG--CGAGACGTGGCACTGG-CGTCGG-G

Query  AGACCG--CGGTTTC-TGGAGAATAT-CCGCCAGGCGTATT-TAGTGCA-TTGCCACGAC
       |||.||  ||| .|| |.|||..||| ||||| ..|||||| .| | .| |||||.|| |
Target AGAGCGTCCGG-CTCGTCGAGGTTATCCCGCC-TCCGTATTCGA-T-AATTTGCCCCG-C

Query  TT-TTAGAACG--TA-CGG-GA--ATGGGAGAAAAAGGCAGTATTACCGCATTTTATACG
       || .|.|||||  .| .|| ||  | |.|||     ||.||.|||||.||.|||||||||
Target TTGCTGGAACGCCCAGGGGCGACCA-GCGAG-----GGAAGCATTACTGCCTTTTATACG

Query  GTACTGGTGGAAGGCGATGATATGA--ATGAGCCGTTGGCGGATGAAGTCCGTTC-ACTG
       ||||||.|||||.||||.|| | ||  ..||.|||.|||||||||||.|.||.|| | |.
Target GTACTGCTGGAAAGCGAGGA-A-GAGGCGGACCCGATGGCGGATGAAATTCGCTCTA-TC

Query  CTTGATGGACATATTGTA-CT-ATCCCGACGGCTTGCAGAG-AGGGGGCATTATCCTGCC
       |||||.||.|| ..|||| || | .|.||..|||.||.|.| | |||.|||||.||.||.
Target CTTGACGGTCA-CCTGTATCTGA-GCAGAAAGCTGGCCGGGCA-GGGACATTACCCGGCA

Query  ATTGACGTGT--TGGCAA-CGCTCAGCCGCGTTTTT
       ||.||  |||  ||..|| || |.||||||||||||
Target ATCGA--TGTACTGAAAAGCG-TAAGCCGCGTTTTT
```
### AI Disclaimer: 
I used AI to help me run the file through my function and put the results in this markdown.