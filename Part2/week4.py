#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 19:01:59 2022

@author: brian
"""

import week3 as w3

from collections import defaultdict
import numpy as np

w3.GenerateSpectrum_cyclic('NQEL')

def cyclopeptide_score(prot_sequence,spectrum,linear=False):
    experimental_spectrum = [int(i) for i in spectrum.split()]
    if linear:
        
        theoretical_spectrum = w3.linear_spectrum(prot_sequence)
    else:
        theoretical_spectrum = w3.cyclic_spectrum(prot_sequence)

    
    experimental_spect = defaultdict(int)
    for exp_mass in experimental_spectrum:
        experimental_spect[exp_mass] = experimental_spect[exp_mass] + 1
        
    print(experimental_spect)
        
    theoretical_spect = defaultdict(lambda: 0)
    for the_mass in theoretical_spectrum:
        theoretical_spect[the_mass] = theoretical_spect[the_mass] + 1
    print(theoretical_spect)
    
    matches = 0
    matches2 = 0
    matches3 = 0
    for the_mass in theoretical_spect.keys():
        matches2 += np.min([theoretical_spect[the_mass],experimental_spect[the_mass]])
        if experimental_spect[the_mass] != 0:
            if theoretical_spect[the_mass] == experimental_spect[the_mass]:
                matches += theoretical_spect[the_mass]
                matches3 += theoretical_spect[the_mass]
            else:
                print('multiplicity?',theoretical_spect[the_mass],experimental_spect[the_mass])
                matches += np.min([theoretical_spect[the_mass],experimental_spect[the_mass]])
                #matches += theoretical_spect[the_mass]
    return matches,matches2,matches3
    
    """
    matches = 0
    for the_mass in theoretical_spectrum:
        for exp_mass in experimental_spectrum:
            if exp_mass == the_mass:
                matches = matches+1
                break
    return matches
    """
    """
    matches = 0
    for the_mass in list(set(theoretical_spectrum)):
        if np.isin(the_mass,experimental_spectrum):
            matches = matches+1
    return matches
    """

cyclopeptide_score('NQEL','0 99 113 114 128 227 257 299 355 356 370 371 484')

peptide = 'FQQPAYCSTHRCMRSGFYMGRQQHILRNHKAAWDEFPFQ'
spect = """0 57 57 71 71 71 87 87 97 99 103 103 113 113 113 113 114 115 115 128 128 128 128 129 131 131 131 137 137 142 144 147 147 147 147 147 156 156 156 163 163 168 186 188 190 199 204 213 224 225 226 226 234 234 234 244 245 246 246 250 250 256 257 259 259 262 266 268 269 269 270 270 271 275 275 275 276 281 291 294 296 301 310 326 328 330 331 337 337 344 349 351 353 353 355 363 363 363 367 371 372 373 374 374 375 382 382 383 390 391 393 401 401 403 403 412 418 422 424 424 428 430 434 439 441 443 444 452 454 456 457 458 459 476 476 490 496 498 498 500 500 501 505 505 507 514 515 515 519 519 521 521 521 521 522 527 529 531 550 555 559 562 570 571 571 571 572 576 577 585 587 587 589 591 600 608 608 614 615 620 627 628 632 632 633 637 642 642 642 648 649 649 650 652 654 662 668 668 671 671 676 678 686 689 690 699 700 701 702 707 711 711 713 719 722 722 729 733 734 739 745 745 746 747 755 764 765 767 771 775 777 777 779 783 784 786 789 796 796 797 798 802 816 818 818 820 823 824 825 826 831 837 842 842 846 847 853 857 859 862 870 874 874 876 876 877 880 892 894 897 901 910 911 911 912 924 924 924 925 933 933 933 935 937 939 945 945 945 946 951 956 958 963 963 965 965 970 972 978 979 981 983 990 1005 1005 1009 1013 1015 1017 1020 1021 1022 1024 1034 1039 1040 1042 1048 1052 1053 1066 1066 1067 1071 1072 1074 1076 1076 1077 1080 1083 1085 1089 1092 1092 1093 1093 1096 1096 1098 1101 1108 1112 1112 1118 1123 1130 1142 1146 1147 1150 1161 1161 1167 1168 1169 1169 1169 1170 1173 1179 1186 1187 1189 1191 1195 1198 1199 1199 1203 1203 1211 1213 1214 1220 1221 1221 1224 1226 1227 1229 1240 1243 1243 1248 1252 1255 1260 1265 1270 1274 1274 1282 1284 1286 1292 1297 1298 1298 1298 1300 1300 1301 1310 1314 1325 1327 1330 1331 1333 1334 1335 1336 1338 1342 1345 1346 1347 1352 1354 1357 1358 1361 1366 1368 1368 1374 1384 1387 1395 1397 1399 1402 1411 1416 1425 1429 1429 1431 1433 1433 1438 1438 1440 1445 1445 1445 1446 1448 1451 1454 1456 1460 1461 1461 1462 1464 1466 1470 1473 1474 1487 1494 1496 1496 1497 1499 1499 1504 1513 1518 1522 1522 1524 1525 1532 1533 1542 1543 1551 1553 1560 1561 1564 1566 1570 1573 1573 1574 1576 1577 1582 1587 1592 1593 1593 1596 1601 1602 1602 1604 1607 1611 1613 1617 1621 1622 1624 1625 1627 1644 1645 1653 1655 1657 1659 1664 1666 1667 1674 1680 1685 1688 1689 1690 1696 1700 1701 1704 1707 1710 1710 1713 1716 1717 1720 1720 1721 1721 1724 1727 1729 1735 1741 1755 1756 1758 1764 1767 1769 1772 1774 1777 1784 1787 1788 1788 1790 1792 1794 1798 1800 1801 1803 1811 1813 1819 1823 1827 1829 1836 1836 1837 1841 1843 1846 1848 1851 1852 1855 1857 1857 1857 1859 1863 1869 1875 1882 1890 1892 1895 1897 1900 1900 1903 1905 1914 1914 1914 1916 1916 1923 1925 1925 1928 1930 1936 1940 1946 1950 1950 1951 1952 1953 1955 1966 1966 1970 1971 1985 1985 1987 1988 1992 1993 1995 2003 2004 2010 2011 2017 2020 2022 2023 2025 2028 2029 2034 2037 2037 2050 2053 2053 2056 2058 2058 2063 2068 2070 2075 2080 2083 2086 2087 2092 2093 2095 2097 2098 2100 2107 2108 2122 2123 2124 2124 2132 2132 2132 2137 2138 2140 2145 2149 2150 2151 2157 2159 2164 2166 2167 2174 2176 2181 2184 2184 2185 2189 2193 2195 2197 2200 2208 2208 2210 2211 2215 2221 2226 2231 2234 2235 2236 2237 2239 2244 2245 2251 2253 2255 2260 2263 2272 2276 2279 2279 2280 2287 2292 2293 2295 2296 2298 2299 2303 2303 2306 2315 2321 2326 2332 2334 2341 2344 2344 2348 2349 2355 2356 2358 2358 2359 2363 2364 2364 2366 2367 2373 2374 2378 2378 2381 2388 2390 2396 2401 2407 2416 2419 2419 2423 2424 2426 2427 2429 2430 2435 2442 2443 2443 2446 2450 2459 2462 2467 2469 2471 2477 2478 2483 2485 2486 2487 2488 2491 2496 2501 2507 2511 2512 2514 2514 2522 2525 2527 2529 2533 2537 2538 2538 2541 2546 2548 2555 2556 2558 2563 2565 2571 2572 2573 2577 2582 2584 2585 2590 2590 2590 2598 2598 2599 2600 2614 2615 2622 2624 2625 2627 2629 2630 2635 2636 2639 2642 2647 2652 2654 2659 2664 2664 2666 2669 2669 2672 2685 2685 2688 2693 2694 2697 2699 2700 2702 2705 2711 2712 2718 2719 2727 2729 2730 2734 2735 2737 2737 2751 2752 2756 2756 2767 2769 2770 2771 2772 2772 2776 2782 2786 2792 2794 2797 2797 2799 2806 2806 2808 2808 2808 2817 2819 2822 2822 2825 2827 2830 2832 2840 2847 2853 2859 2863 2865 2865 2865 2867 2870 2871 2874 2876 2879 2881 2885 2886 2886 2893 2895 2899 2903 2909 2911 2919 2921 2922 2924 2928 2930 2932 2934 2934 2935 2938 2945 2948 2950 2953 2955 2958 2964 2966 2967 2981 2987 2993 2995 2998 3001 3001 3002 3002 3005 3006 3009 3012 3012 3015 3018 3021 3022 3026 3032 3033 3034 3037 3042 3048 3055 3056 3058 3063 3065 3067 3069 3077 3078 3095 3097 3098 3100 3101 3105 3109 3111 3115 3118 3120 3120 3121 3126 3129 3129 3130 3135 3140 3145 3146 3148 3149 3149 3152 3156 3158 3161 3162 3169 3171 3179 3180 3189 3190 3197 3198 3200 3200 3204 3209 3218 3223 3223 3225 3226 3226 3228 3235 3248 3249 3252 3256 3258 3260 3261 3261 3262 3266 3268 3271 3274 3276 3277 3277 3277 3282 3284 3284 3289 3289 3291 3293 3293 3297 3306 3311 3320 3323 3325 3327 3335 3338 3348 3354 3354 3356 3361 3364 3365 3368 3370 3375 3376 3377 3380 3384 3386 3387 3388 3389 3391 3392 3395 3397 3408 3412 3421 3422 3422 3424 3424 3424 3425 3430 3436 3438 3440 3448 3448 3452 3457 3462 3467 3470 3474 3479 3479 3482 3493 3495 3496 3498 3501 3501 3502 3508 3509 3511 3519 3519 3523 3523 3524 3527 3531 3533 3535 3536 3543 3549 3552 3553 3553 3553 3554 3555 3561 3561 3572 3575 3576 3580 3592 3599 3604 3610 3610 3614 3621 3624 3626 3626 3629 3629 3630 3630 3633 3637 3639 3642 3645 3646 3646 3648 3650 3651 3655 3656 3656 3669 3670 3674 3680 3682 3683 3688 3698 3700 3701 3702 3705 3707 3709 3713 3717 3717 3732 3739 3741 3743 3744 3750 3752 3757 3757 3759 3759 3764 3766 3771 3776 3777 3777 3777 3783 3785 3787 3789 3789 3789 3797 3798 3798 3798 3810 3811 3811 3812 3821 3825 3828 3830 3842 3845 3846 3846 3848 3848 3852 3860 3863 3865 3869 3875 3876 3880 3880 3885 3891 3896 3897 3898 3899 3902 3904 3904 3906 3920 3924 3925 3926 3926 3933 3936 3938 3939 3943 3945 3945 3947 3951 3955 3957 3958 3967 3975 3976 3977 3977 3983 3988 3989 3993 4000 4000 4003 4009 4011 4011 4015 4020 4021 4022 4023 4032 4033 4036 4044 4046 4051 4051 4054 4054 4060 4068 4070 4072 4073 4073 4074 4080 4080 4080 4085 4089 4090 4090 4094 4095 4102 4107 4108 4114 4114 4122 4131 4133 4135 4135 4137 4145 4146 4150 4151 4151 4151 4152 4160 4163 4167 4172 4191 4193 4195 4200 4201 4201 4201 4201 4203 4203 4207 4207 4208 4215 4217 4217 4221 4222 4222 4224 4224 4226 4232 4246 4246 4263 4264 4265 4266 4268 4270 4278 4279 4281 4283 4288 4292 4294 4298 4298 4300 4304 4310 4319 4319 4321 4321 4329 4331 4332 4339 4340 4340 4347 4348 4348 4349 4350 4351 4355 4359 4359 4359 4367 4369 4369 4371 4373 4378 4385 4385 4391 4392 4394 4396 4412 4421 4426 4428 4431 4441 4446 4447 4447 4447 4451 4452 4452 4453 4453 4454 4456 4460 4463 4463 4465 4466 4472 4472 4476 4476 4477 4478 4488 4488 4488 4496 4496 4497 4498 4509 4518 4523 4532 4534 4536 4554 4559 4559 4566 4566 4566 4575 4575 4575 4575 4575 4578 4580 4585 4585 4591 4591 4591 4593 4594 4594 4594 4594 4607 4607 4608 4609 4609 4609 4609 4619 4619 4623 4625 4635 4635 4651 4651 4651 4665 4665 4722"""

cyclopeptide_score(peptide,spect)


def spectrum_convolution(spectrum):
    var = []
    spectrum = [int(i) for i in spectrum.split(' ')]
    for x in range(len(spectrum)):
        for y in range(x,len(spectrum)):
            if spectrum[y]-spectrum[x] != 0:
                var.append(spectrum[y]-spectrum[x])
    return var

def prettyprint(x):
    print(' '.join([str(i) for i in x]))
    
prettyprint(spectrum_convolution('0 87 97 97 103 113 128 137 137 163 184 200 224 234 240 241 260 265 276 321 327 337 337 347 362 373 378 404 424 424 460 465 474 475 484 501 521 541 561 578 587 588 597 602 638 638 658 684 689 700 715 725 725 735 741 786 797 802 821 822 828 838 862 878 899 925 925 934 949 959 965 965 975 1062'))
