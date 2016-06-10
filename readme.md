# Neptune Computational Biology - Final Project

# DropSeq Data Analysis

![Figure 1 - DropSeq](Drop-Seq.gif?raw=true)

## Introduction and Goal

DropSeq is a new single cell RNAseq method. The power of the technique is it allows you to sequence single cells and assess their identity after sequencing. So it is not required to sort the cells before sequencing.

The goal of my project is to sort out and make some meaning out of DropSeq Single Cell Sequencing Data. Since I don't have any DropSeq data, I just made a simulator that will simulate DropSeq reads.
DropSeq generates RNAseq reads from a lot of cells in a way that each cell has a 12 base sequence barcode and mRNA reads of each cells is starting with its unique barcode. After the barcode there is a 8 base long Unique Moleculer Identifier (UMI) which is unique for every single mRNA molecule and then ~50base long read of the mRNA.

I'll use Python to make a function that simulates DropSeq data. I'll generate a function (seqsim.py) that'd generate 100 different barcodes and 10000 UMI+mRNA reads each carrying one of those barcodes.

## Methods

The tools I used were... See analysis files at (links to analysis files).

## Results



In Figure 1...

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


