This script takes two arguments: a dir to crawl and a dir to compare to. It will find the files that exist in the first dir that are missing from the second.
It also find files that exists in both dirs and has different sizes.

##How to use the script
```
python3 missing_file_finder.py <dir> <dir to compare with>
```

##Example output
In this example, two directories with the following structure are used as input to the script:
```
test
  ├── dir1
  │   ├── hej.txt
  │   ├── heter_nat
  │   │   └── hej.txt
  │   ├── same_name_different_content.jpg
  │   └── wallpaper3.jpg
  └── dir2
      ├── hej.txt
      ├── heter_nat_annat
      └── same_name_different_content.jpg
```
This is the output of the script:
```
▶ python3 missing_file_finder.py test/dir1 test/dir2
= SUMMARY =
 total size:               729508
 total size backup:        134267
 total nr of files:        3
 total nr of files backup: 2
===================
== MISSING FILES ==
test/dir1/wallpaper3.jpg
== SIZE DIFF FILES ==
test/dir1/same_name_different_content.jpg
```
The output shows that wallpaper3.jpg exists in `test/dir1` but not in `test/dir2`.
We can also see that `same_name_different_content.jpg` exists in both dirs but has different size.
