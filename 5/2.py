
from ast import literal_eval
input = ["959,103 -> 139,923", "899,63 -> 899,53", "591,871 -> 364,644", "739,913 -> 310,484", "460,309 -> 460,705", "351,389 -> 351,837", "420,55 -> 420,541", "916,520 -> 382,520", "136,604 -> 295,604", "343,59 -> 142,59", "951,206 -> 806,206", "984,950 -> 61,27", "739,388 -> 988,388", "374,370 -> 644,370", "403,504 -> 798,899", "943,535 -> 229,535", "149,227 -> 583,661", "62,126 -> 62,352", "131,391 -> 131,717", "254,944 -> 254,220", "572,111 -> 572,47", "336,249 -> 830,743", "898,858 -> 203,163", "203,320 -> 825,942", "19,318 -> 19,120", "740,432 -> 740,39", "591,383 -> 220,754", "445,592 -> 19,592", "202,370 -> 837,370", "473,916 -> 600,789", "118,955 -> 884,189", "377,376 -> 533,532", "160,264 -> 160,62", "627,572 -> 627,679", "217,690 -> 217,629", "685,323 -> 866,504", "391,309 -> 493,207", "872,776 -> 357,776", "116,326 -> 116,426", "82,900 -> 832,900", "594,862 -> 594,593", "802,636 -> 802,223", "862,226 -> 862,787", "313,573 -> 834,573", "145,631 -> 13,499", "545,433 -> 420,308", "427,623 -> 427,808", "898,120 -> 511,120", "859,811 -> 859,28", "715,958 -> 715,893", "115,234 -> 484,234", "125,253 -> 50,253", "737,265 -> 158,265", "523,965 -> 523,983", "118,51 -> 118,766", "455,774 -> 455,357", "680,881 -> 925,881", "191,186 -> 187,186", "821,629 -> 792,658", "397,906 -> 397,962", "988,811 -> 988,427", "91,733 -> 519,733", "46,172 -> 566,172", "740,619 -> 880,759", "609,465 -> 609,702", "289,211 -> 289,620", "622,135 -> 622,929", "113,53 -> 872,53", "559,713 -> 559,132", "894,237 -> 211,920", "237,259 -> 237,39", "738,542 -> 976,542", "163,34 -> 525,34", "681,672 -> 264,255", "37,827 -> 722,827", "60,803 -> 514,349", "433,866 -> 433,257", "379,493 -> 379,643", "697,588 -> 192,83", "875,646 -> 318,89", "634,983 -> 634,111", "636,69 -> 636,41", "911,780 -> 701,570", "792,71 -> 956,71", "682,338 -> 608,412", "257,768 -> 450,575", "112,25 -> 795,708", "730,86 -> 730,65", "966,785 -> 789,608", "390,263 -> 483,356", "90,852 -> 90,471", "507,914 -> 769,914", "803,535 -> 803,245", "710,787 -> 570,787", "138,842 -> 270,710", "862,988 -> 862,656", "56,408 -> 849,408", "16,10 -> 979,973", "982,14 -> 12,984", "647,915 -> 38,306", "797,487 -> 19,487", "539,933 -> 924,933", "509,734 -> 176,734", "813,505 -> 976,505", "474,987 -> 474,896", "21,200 -> 164,200", "986,973 -> 31,18", "919,830 -> 111,22", "32,574 -> 456,150", "743,595 -> 842,595", "623,306 -> 722,306", "878,367 -> 519,367", "924,221 -> 924,231", "86,950 -> 773,263", "950,248 -> 537,248", "149,155 -> 962,968", "449,568 -> 179,568", "186,304 -> 868,986", "921,320 -> 639,602", "602,262 -> 602,500", "602,33 -> 602,248", "380,731 -> 423,774", "535,110 -> 638,110", "552,317 -> 552,75", "173,667 -> 173,847", "707,480 -> 195,480", "833,398 -> 267,964", "276,716 -> 413,716", "342,816 -> 922,816", "24,184 -> 715,875", "762,330 -> 717,285", "718,886 -> 718,551", "707,834 -> 707,704", "479,578 -> 161,896", "145,297 -> 145,435", "760,651 -> 536,875", "954,629 -> 954,816", "305,949 -> 305,919", "55,132 -> 55,233", "469,85 -> 439,85", "653,990 -> 536,990", "876,531 -> 432,87", "698,207 -> 698,672", "11,70 -> 766,825", "591,357 -> 30,918", "697,987 -> 697,823", "610,903 -> 370,663", "319,678 -> 319,504", "337,150 -> 309,150", "876,57 -> 311,57", "673,268 -> 345,596", "895,364 -> 518,741", "327,662 -> 941,48", "77,709 -> 110,742", "194,78 -> 661,78", "587,24 -> 825,24", "503,317 -> 719,317", "459,632 -> 704,387", "717,292 -> 835,292", "912,927 -> 72,87", "510,527 -> 146,527", "336,771 -> 336,266", "566,961 -> 496,961", "969,335 -> 122,335", "925,443 -> 925,397", "316,812 -> 606,812", "815,795 -> 116,795", "169,36 -> 354,36", "358,274 -> 389,274", "302,147 -> 839,684", "762,372 -> 972,372", "172,721 -> 682,211", "265,150 -> 248,167", "753,559 -> 307,559", "823,121 -> 823,126", "498,856 -> 498,135", "75,977 -> 75,381", "541,297 -> 541,320", "735,108 -> 866,108", "434,907 -> 868,907", "915,959 -> 255,959", "967,666 -> 967,209", "361,600 -> 361,222", "314,580 -> 314,497", "175,989 -> 523,641", "957,97 -> 311,743", "956,227 -> 12,227", "95,364 -> 95,742", "857,141 -> 193,805", "388,651 -> 468,731", "582,177 -> 324,177", "68,272 -> 68,720", "543,490 -> 910,490", "508,281 -> 902,281", "823,380 -> 823,296", "23,10 -> 946,933", "813,70 -> 813,450", "881,893 -> 598,893", "535,781 -> 973,781", "80,890 -> 909,61", "604,630 -> 307,927", "836,917 -> 184,917", "76,727 -> 10,727", "727,235 -> 727,578", "629,80 -> 892,80", "110,655 -> 663,102", "985,12 -> 11,986", "830,656 -> 830,761", "660,869 -> 660,543", "381,340 -> 381,562", "392,735 -> 417,735", "855,24 -> 320,24", "801,669 -> 278,146", "730,964 -> 107,964", "523,158 -> 385,20", "27,833 -> 27,987", "569,707 -> 500,707", "527,732 -> 527,424", "74,88 -> 273,287", "143,974 -> 143,735", "247,388 -> 813,954", "577,14 -> 945,382", "49,43 -> 953,947", "332,210 -> 332,143", "69,280 -> 949,280", "25,923 -> 904,44", "306,569 -> 306,470", "158,273 -> 113,228", "771,355 -> 694,278", "515,115 -> 245,385", "427,381 -> 427,729", "16,987 -> 987,16", "319,463 -> 319,234", "854,977 -> 66,189", "794,194 -> 794,183", "576,65 -> 576,843", "37,964 -> 734,964", "740,920 -> 740,877", "245,487 -> 245,957", "404,794 -> 853,794", "660,656 -> 660,756", "921,605 -> 127,605", "650,894 -> 916,894", "968,893 -> 481,406", "986,979 -> 21,14", "154,303 -> 498,647", "720,338 -> 229,338", "62,936 -> 62,897", "55,820 -> 55,923", "812,31 -> 551,31", "338,466 -> 951,466", "663,492 -> 775,604", "449,602 -> 39,602", "44,403 -> 44,144", "58,62 -> 339,62", "713,730 -> 713,502", "704,525 -> 976,797", "372,709 -> 372,680", "709,387 -> 153,387", "922,103 -> 615,103", "629,839 -> 121,839", "206,722 -> 529,722", "232,556 -> 422,746", "300,470 -> 300,726", "376,820 -> 622,574", "834,25 -> 255,604", "271,200 -> 271,875", "804,934 -> 872,934", "900,753 -> 900,632", "604,323 -> 604,70", "890,911 -> 890,41", "464,169 -> 812,169", "850,196 -> 850,903", "34,574 -> 34,54", "718,59 -> 462,315", "431,923 -> 737,923", "433,573 -> 433,420", "297,478 -> 297,775", "756,545 -> 544,545", "247,708 -> 247,702", "736,835 -> 173,272", "319,85 -> 319,827", "931,775 -> 683,775", "292,315 -> 451,315", "397,435 -> 380,435", "987,978 -> 82,73", "227,349 -> 227,724", "349,741 -> 899,191", "965,325 -> 765,125", "849,306 -> 88,306", "516,548 -> 516,902", "919,395 -> 568,395", "736,507 -> 192,507", "960,782 -> 196,18", "431,413 -> 510,492", "911,696 -> 911,830", "888,225 -> 174,225", "57,790 -> 57,953", "858,399 -> 119,399", "59,302 -> 290,302", "456,907 -> 456,599", "374,743 -> 374,565", "183,107 -> 183,171", "58,699 -> 288,699", "886,970 -> 109,193", "940,395 -> 806,261", "781,480 -> 596,665", "456,724 -> 265,724", "414,406 -> 299,521", "115,898 -> 115,863", "34,543 -> 34,496", "900,843 -> 900,457", "165,209 -> 189,209", "976,627 -> 539,190", "252,202 -> 137,202", "584,339 -> 550,373", "580,153 -> 380,353", "232,412 -> 650,830", "910,833 -> 88,11", "418,245 -> 829,245", "298,823 -> 907,214", "91,876 -> 495,876", "315,874 -> 650,539", "907,635 -> 365,635", "339,313 -> 320,313", "362,435 -> 362,938", "152,664 -> 152,391", "253,210 -> 272,210", "216,396 -> 216,726", "852,912 -> 15,75", "882,828 -> 689,828", "674,533 -> 674,523", "469,719 -> 469,79", "733,169 -> 665,101", "734,632 -> 717,632", "615,565 -> 615,114", "979,720 -> 243,720", "827,125 -> 827,919", "605,419 -> 601,419", "749,13 -> 433,329", "990,902 -> 990,843", "186,679 -> 186,457", "374,796 -> 736,796", "133,867 -> 133,801", "757,622 -> 812,567", "351,179 -> 351,509", "214,748 -> 575,748", "177,903 -> 861,219", "747,981 -> 747,64", "588,125 -> 588,557", "464,338 -> 769,338", "645,669 -> 125,149", "579,352 -> 138,352", "77,605 -> 520,605", "698,816 -> 698,917", "112,943 -> 112,834", "731,720 -> 724,720", "887,440 -> 976,351", "676,301 -> 676,741", "870,732 -> 870,648", "250,826 -> 413,826", "399,720 -> 543,864", "834,93 -> 468,459", "415,475 -> 415,641", "793,415 -> 47,415", "365,476 -> 365,31", "195,154 -> 813,154", "503,605 -> 773,605", "553,121 -> 851,121", "25,420 -> 423,818", "943,110 -> 258,110", "775,436 -> 826,436", "16,161 -> 16,889", "702,555 -> 920,555", "589,858 -> 533,802", "932,404 -> 932,539", "647,275 -> 647,962", "87,179 -> 326,179", "931,588 -> 931,287", "868,96 -> 557,96", "879,28 -> 875,28", "375,132 -> 287,44", "484,352 -> 644,512", "448,566 -> 448,214", "734,460 -> 717,460", "550,379 -> 550,674", "964,184 -> 820,328", "167,504 -> 387,504", "594,777 -> 952,777", "328,712 -> 837,712", "600,773 -> 546,773", "955,954 -> 82,81", "863,790 -> 863,86", "831,773 -> 32,773", "987,11 -> 19,979", "901,878 -> 901,177", "427,341 -> 721,635", "690,835 -> 567,835", "557,724 -> 14,181", "591,20 -> 205,406", "846,865 -> 846,859", "644,646 -> 742,548", "187,376 -> 187,563", "367,806 -> 250,923", "332,731 -> 468,731", "378,431 -> 469,431", "844,949 -> 844,452", "172,320 -> 735,320", "597,639 -> 633,639", "353,831 -> 353,307", "355,392 -> 465,392", "624,179 -> 548,255", "441,928 -> 401,888", "442,680 -> 442,569", "567,385 -> 908,44", "10,561 -> 603,561", "851,289 -> 13,289", "832,143 -> 832,64", "366,851 -> 67,851", "890,404 -> 333,961", "83,22 -> 963,902", "10,783 -> 821,783", "369,481 -> 369,611", "943,356 -> 846,356", "675,95 -> 335,435", "442,928 -> 442,764", "500,643 -> 334,643", "90,207 -> 620,207", "520,412 -> 745,187", "586,89 -> 613,89", "411,424 -> 595,424", "938,650 -> 232,650", "216,773 -> 76,773", "895,690 -> 895,294", "250,886 -> 250,605", "296,422 -> 863,989", "534,626 -> 534,707", "577,608 -> 52,83", "61,674 -> 714,21", "844,126 -> 844,694", "565,541 -> 253,229", "62,24 -> 986,948", "588,901 -> 588,212", "541,508 -> 541,141", "516,376 -> 589,449", "390,215 -> 749,215", "324,878 -> 296,850", "592,408 -> 592,158", "433,207 -> 172,207", "139,72 -> 139,121", "471,676 -> 268,676", "374,433 -> 374,95", "672,459 -> 640,427", "348,577 -> 843,82", "903,466 -> 903,348", "437,759 -> 726,470", "152,101 -> 325,274", "933,897 -> 335,897", "516,877 -> 505,866", "890,715 -> 570,715", "78,124 -> 871,917", "360,645 -> 967,645", "645,271 -> 645,57", "693,878 -> 693,159", "49,77 -> 49,744", "935,914 -> 97,76", "941,726 -> 941,464", "756,985 -> 756,480", "887,378 -> 887,529", "405,925 -> 405,533", "533,156 -> 201,156", "565,535 -> 120,90", "51,15 -> 967,931", "660,218 -> 660,339", "522,682 -> 571,682", "958,899 -> 729,899", "521,687 -> 288,687", "643,148 -> 468,323", "989,971 -> 68,50", "729,273 -> 311,691", "245,205 -> 305,205", "634,747 -> 634,605", "280,407 -> 488,199", "109,931 -> 706,334", "849,694 -> 615,928", "794,84 -> 218,84", "669,184 -> 865,184", "936,834 -> 234,132", "691,445 -> 914,668", "423,161 -> 515,69", "81,674 -> 37,674", "292,423 -> 292,741", "188,306 -> 844,962", "204,309 -> 204,705", "961,652 -> 746,652", "985,987 -> 11,13", "139,153 -> 936,950", "436,978 -> 244,978", "921,633 -> 921,340", "872,63 -> 233,63"]

testinput = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def newLine(lineStart,lineEnd):
        return Line(lineStart,lineEnd)

size = 1000

lines: Line = []
def makeLines():
    for x in input:
        start = literal_eval(x.split(" -> ")[0])
        end = literal_eval(x.split(" -> ")[1])
        lines.append(Line.newLine(start,end))


pathboard = [[0] * size for _ in range(size)]

def drawLines(line: Line):
    if line.start[0] == line.end[0]:
        for i in range(min(line.start[1],line.end[1]),max(line.start[1],line.end[1])+1):
            pathboard[i][line.start[0]] += 1
        return
    if line.start[1] == line.end[1]:
        for i in range(min(line.start[0], line.end[0]),max(line.start[0], line.end[0])+1):
            pathboard[line.start[1]][i] +=1
        return

    diaglen = abs(line.start[0] - line.end[0])

    if line.start[0] < line.end[0] and line.start[1] < line.end[1]:
        for i in range(0,diaglen+1):
            pathboard[line.start[1]+i][line.start[0]+i] += 1
        return
    if line.start[0] > line.end[0] and line.start[1] > line.end[1]:
        for i in range(0,diaglen+1):
            pathboard[line.end[1]+i][line.end[0]+i] += 1
        return


    if line.start[0] < line.end[0] and line.start[1] > line.end[1]:
        for i in range(0,diaglen+1):
            pathboard[line.start[1]-i][line.start[0]+i] += 1
        return

    if line.start[0] > line.end[0] and line.start[1] < line.end[1]:
        for i in range(0,diaglen+1):
            pathboard[line.start[1]+i][line.start[0]-i] += 1
        return




def printBoard():
    for x in pathboard:
        print(x)

def evalOverlap():
    hits = 0
    for x in pathboard:
        for y in x:
            if y >= 2:
                hits += 1
    return hits
def main():
    makeLines()
    for line in lines:
        drawLines(line)
    printBoard()
    print(evalOverlap())

main()