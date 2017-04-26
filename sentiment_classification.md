# Sentiment Classification

## Bag of Words

### Reviews
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7256644206419125 | 0.7482976735786503 | 0.8043944330874894 |
| Sub Recall    | 0.8040082421967479 | 0.7614419812513737 | 0.7931071691062436 |
| Sub F-Measure | 0.7615798853150174 | 0.7542024240530665 | 0.7983862210404051 |
| Obj Precision | 0.7787688944340239 | 0.7563309081623577 | 0.7959650444285168 |
| Obj Recall    | 0.6906713829904408 | 0.7413146198635637 | 0.8061683762354311 |
| Obj F-Measure | 0.7302103466763984 | 0.7480831301001734 | 0.8007201656984447 |

### Reviews (withou punctuation)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7272945123009584 | 0.7478327538703120 | 0.8052955033501675 |
| Sub Recall    | 0.7979400546084245 | 0.7596986729843143 | 0.7918494584198733 |
| Sub F-Measure | 0.7597551290542457 | 0.7531364111325874 | 0.7981041430261859 |
| Obj Precision | 0.7748556890979511 | 0.7549372970133466 | 0.7951526684577035 |
| Obj Recall    | 0.6956805450986957 | 0.7413146125595871 | 0.8072275234484430 |
| Obj F-Measure | 0.7313649624731972 | 0.7474330600547505 | 0.8007593641632951 |

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7264994547908981 | 0.7118501743172432 | 0.7620475910693232 |
| Sub Recall    | 0.6989950994212426 | 0.7312111799730026 | 0.7569626593447710 |
| Sub F-Measure | 0.7105639801503763 | 0.7206720397107672 | 0.7589841283778297 |
| Obj Precision | 0.7075036554765142 | 0.7220960628589179 | 0.7580957564744392 |
| Obj Recall    | 0.7297064414938326 | 0.7005798943533346 | 0.7617484585444304 |
| Obj F-Measure | 0.7167368777983555 | 0.7103579750753324 | 0.7594155712253760 |                                                              

## Word Bigrams

### Reviews
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7877015607357831 | 0.7873383850732866 | 0.8012065598784840 |
| Sub Recall    | 0.8294945214819205 | 0.7912533151532486 | 0.7993296093765141 |
| Sub F-Measure | 0.8076147381427978 | 0.7891024031633328 | 0.7997720923416257 |
| Obj Precision | 0.8198947563643424 | 0.7901675099832671 | 0.7999443461607650 |
| Obj Recall    | 0.7749000840346856 | 0.7856689454099814 | 0.8003433818521891 |
| Obj F-Measure | 0.7962199734092545 | 0.7877135424646923 | 0.7996610385288607 |

### Reviews (without punctuation)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7881576918210245 | 0.7798151108248736 | 0.8073194971274150 |
| Sub Recall    | 0.8189688800929533 | 0.7961081710170612 | 0.7602055129636334 |
| Sub F-Measure | 0.8028950987919972 | 0.7876067394924937 | 0.7820652126495558 |
| Obj Precision | 0.8116514537476714 | 0.7919373811115527 | 0.7742589611162758 |
| Obj Recall    | 0.7786957659042386 | 0.7745695230960992 | 0.8167176045995186 |
| Obj F-Measure | 0.7944000127426434 | 0.7828605619643335 | 0.7940083388109925 |

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7289955108849492 | 0.6660535051391998 | 0.6394763311086551 |
| Sub Recall    | 0.6158485555509785 | 0.7680618795819671 | 0.8293178017679323 |
| Sub F-Measure | 0.6673005035448041 | 0.7131256213920800 | 0.7210953217684143 |
| Obj Precision | 0.6670501261892092 | 0.7258943908598970 | 0.7557242714788271 |
| Obj Recall    | 0.7698692583318165 | 0.6138163628358477 | 0.5280667279616383 |
| Obj F-Measure | 0.7145686438557686 | 0.6646341159643072 | 0.6189813354047569 |

## Part of Speech

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 0.7268406286566291 | 0.7102313795034665 | 0.7602305950667911 |
| Sub Recall    | 0.7029891670340567 | 0.7262242682121491 | 0.7542928051253270 |
| Sub F-Measure | 0.7129721944746303 | 0.7174024596635754 | 0.7562934206320246 |
| Obj Precision | 0.7102609999689748 | 0.7185567184785837 | 0.7557547926985034 |
| Obj Recall    | 0.7293756468279950 | 0.7004916915318378 | 0.7590782488647916 |
| Obj F-Measure | 0.7181116858662572 | 0.7085926497859509 | 0.7565255154676335 |

## TF-IDF

### Reviews
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 
| Sub Recall    | 
| Sub F-Measure | 
| Obj Precision | 
| Obj Recall    | 
| Obj F-Measure | 

### Reviews (withou punctuation)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 
| Sub Recall    | 
| Sub F-Measure | 
| Obj Precision | 
| Obj Recall    | 
| Obj F-Measure | 

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 
| Sub Recall    | 
| Sub F-Measure | 
| Obj Precision | 
| Obj Recall    | 
| Obj F-Measure | 


## Bigrams / TF-IDF / Part of Speech

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 
| Sub Recall    | 
| Sub F-Measure | 
| Obj Precision | 
| Obj Recall    | 
| Obj F-Measure | 


## Bag of Words / Bigrams / TF-IDF / Part of Speech

### Reviews (without punctuation, without stopwords)
|   | Naive Bayes | SVM | Maximum Entropy |
|---|---|---|---|
| Sub Precision | 
| Sub Recall    | 
| Sub F-Measure | 
| Obj Precision | 
| Obj Recall    | 
| Obj F-Measure | 



