## Առաջադրանք 2: Ստեղծենք նեյրոնային ցանցը

Մի հատ թաքնված շերտ ենք օգտագործելու ու այդ շերտը ունենալու է երեք նեյրոն։ Ցանց ունենալու է հետևյալ տեսքը։

![Simple neural network](simple-neural-net.png)

Նեյրոնային ցանցը ստեղծելու համար օգտագործելու ենք մի շարք թենզորներ։

### Քայլ 1:
Input շերտը թաքնված շերտին կապվում է 6 կողով։ Ամեն մի կողը ունի կշիռ։ Պիտի զանգված ստեղծենք որ այս 6 կշիռնեը պահի։ Զանգվածի ձևը պիտի համապատասխանի **Առաջադրանք 1**-ում ստեղծած թենզորի չափին, որպեսզի կարողանանք բազմապատկել։

**Hint: An easy way to think about the dimensions of the weight array that we need is to use the number of nodes in the input layer as the size of the first dimension and the number of nodes in the hidden layer as the size of the second dimension.**

Կշիռները փոփոխվող մասն են մեր մոդէլի։ Դրա համար պիտի կշիռների համար օգտագործենք tf.Variable ([documentation](https://www.tensorflow.org/api_docs/python/tf/Variable)). Որպես սկզբնական արժեք կարող ենք օգտագործենք կամ զրոներ ([documentation](https://www.tensorflow.org/api_docs/python/tf/zeros) կամ էլ պատահական արժեքներ ([documentation](https://www.tensorflow.org/api_docs/python/tf/random_normal)). Վերագրի **weights_1** փոփոխականին։

### Քայլ 2:
Շեղում էլ պիտի սահմանենք։ Ամեն նեյրոնի համար ընդամենը մի թիվ է պետք։ Սահմանի 1x3 Variable կամ զրոներով կամ էլ պատահականներով։

### Քայլ 3:
Նորմալիզացված input զանգվածը բազմապատկի **weights_1**-ին. Դրան գումարի **bias_1** և արդյունքը պահի **weighted_sums_1** փոփոխականի մեջ ([documentation](https://www.tensorflow.org/api_docs/python/tf/matmul)).

### Քայլ 4:
Sigmoid activation ֆունկցիան կիրառի **Քայլ 3**-ի արդյունքի վրա։ ([documentation](https://www.tensorflow.org/api_docs/python/tf/sigmoid))։ Արդյունքը վերագրի **activation_1**-ին.

### Քայլ 5:
Կրկնի **Քայլեր 2-4** որ ստեղծես կապը թաքվնած շերտից output շերտ։
Now, we're going to repeat **Steps 2 through 5** for the connections between the hidden layer and the output layer.

### Քայլ 6:
Սահմանի **bias_2** tensorflow variable ոնց որ արեցինք **Քայլ 3**-ում. Output շերտը ունի ընդամենը 1 նեյրոն։

### Քայլ 7:

**activation_1** զանգվածը բազմապատկի **weights_2** զանգվածին. Դրան գումարի **bias_2** և արդյունքը պահի **weighted_sums_2** փոփոխականի մեջ։ Մոտ ենք վերջացնենք նեյրոնային ցանցի կառուցումը։

### Քայլ 8:
Sigmoid activation ֆունկցիան կիրառի **Քայլ 7**-ի արդյունքի վրա, ոնց որ արեցինք **Քայլ 4**-ում։ ([documentation](https://www.tensorflow.org/api_docs/python/tf/sigmoid))։ Արդյունքը վերագրի **activation_2**-ին. Այս **activation_2**-ն մեր ցանցի **_վերջնական արդյունքն է_**։


**Վերջ։ Մոդելը պատրաստ է։**